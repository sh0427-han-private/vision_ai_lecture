import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import test from 'node:test'
import {
  addPadding, adjustBrightness, appleBoxes, convolutionInput, correlate, edgeKernel,
  evaluate, logic, luma, maxPool, nextWeight, overlap, paddingInput, poolInput, regression, sumKernel,
} from '../lesson/calculations.js'

const read = path => readFileSync(new URL(path, import.meta.url), 'utf8')

test('56-slide order, titles, unique identities and 120 minutes match the HTML manifest', () => {
  const manifest = JSON.parse(read('../../docs/two_hour_manifest.json'))
  const entry = read('../slides.md')
  assert.equal((entry.match(/data-lecture-number="cover"/g) ?? []).length, 1)
  const imports = [...entry.matchAll(/^src: \.\/units\/([A-H]\.md)$/gm)].map(match => match[1])
  assert.deepEqual(imports, [...'ABCDEFGH'].map(letter => `${letter}.md`))
  let nextSlide = 0
  const entries = Object.values(manifest.decks).flat()
  for (const [index, file] of imports.entries()) {
    const unit = read(`../units/${file}`)
    const slides = [...unit.matchAll(/^lectureNumber: (P\d+)\nconcept: ([\w-]+)\ntitle: (".*")\n/gm)]
    const block = manifest.blocks[index]
    assert.equal(slides.length, block.end - block.start + 1, file)
    for (const [, number, concept, title] of slides) {
      const expected = entries[nextSlide++]
      assert.equal(number, `P${String(nextSlide).padStart(2, '0')}`)
      assert.equal(concept, expected.concept)
      assert.equal(JSON.parse(title), expected.title)
      assert.ok(unit.includes(`number="${number}" concept="${concept}"`))
    }
  }
  assert.equal(nextSlide, 55)
  assert.equal(new Set(entries.map(slide => slide.concept)).size, 55)
  assert.equal(manifest.blocks.reduce((sum, block) => sum + block.minutes, 0), 120)
})

test('convolution, stride, padding and pooling produce the approved teaching arrays', () => {
  assert.deepEqual(correlate(convolutionInput, edgeKernel), [[-6, 12, 16], [-6, 8, 15], [-4, 2, 7]])
  assert.deepEqual(correlate(convolutionInput, edgeKernel, 2), [[-6, 16], [-4, 7]])
  assert.deepEqual(correlate(paddingInput, sumKernel), [[45]])
  assert.deepEqual(correlate(addPadding(paddingInput, 1), sumKernel), [[12, 21, 16], [27, 45, 33], [24, 39, 28]])
  assert.deepEqual(maxPool(poolInput), [[6, 4], [7, 9]])
})

test('grayscale and light clipping preserve the original image math', () => {
  assert.equal(luma(255, 0, 0), 76)
  assert.equal(luma(0, 255, 0), 150)
  assert.equal(luma(0, 0, 255), 29)
  assert.equal(adjustBrightness(220, 1.5), 255)
})

test('training starts with prediction 1, loss 9 and follows the approved first update', () => {
  assert.deepEqual(regression(0.5), { predicted: 1, loss: 9, gradient: -12 })
  const weight = nextWeight(0.5)
  assert.ok(Math.abs(weight - 1.7) < 1e-12)
  assert.ok(Math.abs(regression(weight).loss - 0.36) < 1e-12)
})

test('thresholds reuse one 100-case cohort including ties at the threshold', () => {
  const counts = threshold => {
    const { tp, fn, fp, tn } = evaluate(threshold)
    return [tp, fn, fp, tn]
  }
  assert.deepEqual(counts(0.3), [20, 0, 30, 50])
  assert.deepEqual(counts(0.5), [18, 2, 4, 76])
  assert.deepEqual(counts(0.7), [11, 9, 2, 78])
  assert.deepEqual(counts(0.6), [18, 2, 4, 76])
  assert.equal(evaluate(0.5).precision, 18 / 22)
  assert.equal(evaluate(0.5).recall, 18 / 20)
  assert.equal(evaluate(1).accuracy, 0.8)
})

test('AND and both XOR presets agree with the shown truth table', () => {
  const points = [[0, 0], [0, 1], [1, 0], [1, 1]]
  assert.deepEqual(points.map(([x, y]) => logic('and', x, y, 1, -1.2, false)), [0, 0, 0, 1])
  assert.deepEqual(points.map(([x, y]) => logic('xor', x, y, 1, -0.5, false)), [0, 1, 1, 1])
  assert.deepEqual(points.map(([x, y]) => logic('xor', x, y, 1, -1, true)), [0, 1, 1, 0])
})

test('IoU uses the same coordinates that draw the apple overlay', () => {
  const result = overlap(appleBoxes.target, appleBoxes.prediction)
  assert.equal(result.intersection, 2340)
  assert.equal(result.union, 5290)
  assert.equal(result.iou, 2340 / 5290)
})
