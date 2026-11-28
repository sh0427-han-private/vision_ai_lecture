// Teaching fixtures from the approved HTML deck at 77d04e1074f1d7c1b20e7f458a137456f1fba02b.
export const convolutionInput = [[1, 2, 3, 0, 1], [4, 5, 6, 1, 0], [7, 8, 9, 2, 1], [0, 1, 2, 3, 1], [1, 0, 1, 2, 3]]
export const edgeKernel = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
export const paddingInput = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
export const sumKernel = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
export const poolInput = [[1, 3, 2, 4], [5, 6, 1, 2], [4, 2, 9, 3], [0, 7, 8, 1]]

export function crop(input, row, col, height, width = height) {
  return input.slice(row, row + height).map(line => line.slice(col, col + width))
}

export function addPadding(input, pad) {
  return Array.from({ length: input.length + pad * 2 }, (_, row) =>
    Array.from({ length: input[0].length + pad * 2 }, (_, col) => input[row - pad]?.[col - pad] ?? 0))
}

function scanWindows(input, height, width, stride, reduce) {
  const rows = Math.floor((input.length - height) / stride) + 1
  const columns = Math.floor((input[0].length - width) / stride) + 1
  return Array.from({ length: rows }, (_, row) =>
    Array.from({ length: columns }, (_, col) => reduce(crop(input, row * stride, col * stride, height, width))))
}

export function correlate(input, weights, stride = 1) {
  return scanWindows(input, weights.length, weights[0].length, stride, window =>
    window.reduce((sum, line, row) => sum + line.reduce((total, value, col) => total + value * weights[row][col], 0), 0))
}

export function maxPool(input) {
  return scanWindows(input, 2, 2, 2, window => Math.max(...window.flat()))
}

export const training = { input: 2, target: 4, initialWeight: 0.5, rate: 0.1 }

export function regression(weight) {
  const predicted = weight * training.input
  const error = predicted - training.target
  return { predicted, loss: error ** 2, gradient: 2 * error * training.input }
}

export function nextWeight(weight) {
  return weight - training.rate * regression(weight).gradient
}

const scoreHistogram = [[0.2, 0, 50], [0.4, 2, 26], [0.6, 7, 2], [0.8, 11, 2]]
export const scoreBins = scoreHistogram.map(([score, defective, normal]) => ({ score, defective, normal }))

export function evaluate(threshold) {
  const counts = { tp: 0, fn: 0, fp: 0, tn: 0 }
  for (const { score, defective, normal } of scoreBins) {
    const positive = score >= threshold
    counts[positive ? 'tp' : 'fn'] += defective
    counts[positive ? 'fp' : 'tn'] += normal
  }
  const { tp, fn, fp, tn } = counts
  return {
    ...counts,
    precision: tp + fp ? tp / (tp + fp) : null,
    recall: tp / (tp + fn),
    accuracy: (tp + tn) / (tp + fn + fp + tn),
  }
}

export const appleBoxes = {
  target: { x: 565, y: 197, width: 60, height: 60 },
  prediction: { x: 580, y: 205, width: 62, height: 65 },
}

export function overlap(first, second) {
  const x = Math.max(first.x, second.x)
  const y = Math.max(first.y, second.y)
  const width = Math.max(0, Math.min(first.x + first.width, second.x + second.width) - x)
  const height = Math.max(0, Math.min(first.y + first.height, second.y + second.height) - y)
  const intersection = width * height
  const union = first.width * first.height + second.width * second.height - intersection
  return { x, y, width, height, intersection, union, iou: union ? intersection / union : 0 }
}

export function luma(red, green, blue) {
  return Math.round(0.299 * red + 0.587 * green + 0.114 * blue)
}

export function adjustBrightness(value, multiplier) {
  return Math.min(255, Math.round(value * multiplier))
}

export function logic(kind, x, y, weight, bias, nonlinear) {
  const signal = weight * x + y + bias
  return Number((kind === 'xor' && nonlinear ? 0.5 - Math.abs(signal) : signal) >= 0)
}
