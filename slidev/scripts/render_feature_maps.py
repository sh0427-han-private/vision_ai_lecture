"""Regenerate P35 with CPU torch==2.9.1 and torchvision==0.24.1."""

import hashlib
import json
from pathlib import Path

import numpy as np
import torch
import torchvision
from PIL import Image
from torchvision.models import SqueezeNet1_1_Weights, squeezenet1_1
from torchvision.transforms.functional import to_pil_image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'docs/assets/vision_task_apple_reference.jpg'
OUT = ROOT / 'figures'
STAGES = (1, 7, 12)
PANEL = 96
GAP = 6


def activation_image(values):
    low, high = np.percentile(values, [2, 99])
    normalized = np.clip((values - low) / max(high - low, 1e-9), 0, 1)
    start = np.array([9, 35, 45])
    end = np.array([251, 230, 112])
    colors = (start + normalized[..., None] * (end - start)).round().astype('uint8')
    return Image.fromarray(colors).resize((PANEL, PANEL), Image.Resampling.NEAREST)


def main():
    weights = SqueezeNet1_1_Weights.IMAGENET1K_V1
    image = Image.open(SOURCE).convert('RGB')
    transform = weights.transforms()
    input_tensor = transform(image)
    mean = torch.tensor(transform.mean)[:, None, None]
    std = torch.tensor(transform.std)[:, None, None]
    source_crop = to_pil_image((input_tensor * std + mean).clamp(0, 1))
    model = squeezenet1_1(weights=weights).eval()

    sheet = Image.new('RGB', (4 * PANEL + 3 * GAP, 3 * PANEL + 2 * GAP), (230, 238, 234))
    stages = []
    activation = input_tensor.unsqueeze(0)
    with torch.inference_mode():
        for layer, block in enumerate(model.features):
            activation = block(activation)
            if layer not in STAGES:
                continue
            channels, height, width = activation.shape[1:]
            features = activation[0].numpy()
            order = np.argsort(-features.var(axis=(1, 2)), kind='stable')[:4].tolist()
            for column, channel in enumerate(order):
                sheet.paste(activation_image(features[channel]), (column * (PANEL + GAP), len(stages) * (PANEL + GAP)))
            stages.append({'layer': layer, 'shape': [height, width, channels], 'channels': order})

    assert [stage['shape'] for stage in stages] == [[111, 111, 64], [27, 27, 256], [13, 13, 512]]
    OUT.mkdir(exist_ok=True)
    source_crop.save(OUT / 'apple-feature-input.png')
    sheet.save(OUT / 'apple-feature-maps.png')
    metadata = {
        'source': str(SOURCE.relative_to(ROOT.parent)).replace('\\', '/'),
        'inputSha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'model': 'SqueezeNet1.1',
        'weights': weights.name,
        'weightsUrl': weights.url,
        'torch': str(torch.__version__),
        'torchvision': torchvision.__version__,
        'preprocessing': {'resizeShortSide': 256, 'centerCrop': 224, 'mean': transform.mean, 'std': transform.std},
        'display': 'Four highest-spatial-variance channels per stage. Each channel uses its own 2nd–99th percentile display range.',
        'stages': stages,
    }
    (OUT / 'apple-feature-maps.json').write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('P35 feature maps:', stages)


if __name__ == '__main__':
    main()
