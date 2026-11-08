import { describe, test, expect } from 'vitest';
import { canBook } from './booking';

// Default fixture, fresh for every call: now = 540 (09:00), room not blocked,
// one existing booking 10:00-11:00.
const fixture = () => ({
  now: 540,
  blocked: false,
  bookings: [{ start: 600, end: 660 }],
});

const check = (
  start: number,
  end: number,
  override: Partial<ReturnType<typeof fixture>> = {}
) => canBook({ ...fixture(), start, end, ...override });

describe('canBook', () => {
  test('T01 AC4: touching after the booking is allowed', () => {
    expect(check(660, 720)).toBe(true);
  });

  test('T02 AC1: start equal to now is rejected', () => {
    expect(check(540, 570)).toBe(false);
  });

  test('T03 AC1: zero duration is rejected', () => {
    expect(check(720, 720)).toBe(false);
  });

  test('T04 AC1: reversed interval is rejected', () => {
    expect(check(750, 720)).toBe(false);
  });

  test('T05 AC1: end past the end of the day is rejected', () => {
    expect(check(1380, 1441)).toBe(false);
  });

  test('T06 AC2: exactly 120 minutes is allowed', () => {
    expect(check(720, 840)).toBe(true);
  });

  test('T07 AC2: 121 minutes is rejected', () => {
    expect(check(720, 841)).toBe(false);
  });

  test('T08 AC4: touching before the booking is allowed', () => {
    expect(check(570, 600)).toBe(true);
  });

  test('T09 AC4: partial overlap is rejected', () => {
    expect(check(630, 690)).toBe(false);
  });

  test('T10 AC4: interval containing the booking is rejected', () => {
    expect(check(570, 690)).toBe(false);
  });

  test('T11 AC4: interval inside the booking is rejected', () => {
    expect(check(615, 645)).toBe(false);
  });

  test('T12 AC4: identical interval is rejected', () => {
    expect(check(600, 660)).toBe(false);
  });

  test('T13 AC3: blocked room is rejected', () => {
    expect(check(660, 720, { blocked: true })).toBe(false);
  });

  test('T14 AC4: no existing bookings, free interval is allowed', () => {
    expect(check(630, 690, { bookings: [] })).toBe(true);
  });

  test('AC5: an Available request leaves the bookings unchanged', () => {
    const bookings = [{ start: 600, end: 660 }];
    const before = JSON.stringify(bookings);
    const result = canBook({ start: 660, end: 720, now: 540, blocked: false, bookings });
    expect(result).toBe(true);
    expect(JSON.stringify(bookings)).toBe(before);
  });

  test('X1 AC1: interval ending exactly at 1440 is allowed', () => {
    expect(check(1380, 1440)).toBe(true);
  });

  test('X2 AC4: gap between two bookings, touching both, is allowed', () => {
    const bookings = [
      { start: 600, end: 660 },
      { start: 720, end: 780 },
    ];
    expect(check(660, 720, { bookings })).toBe(true);
  });
  test('AC1 lower bound: start below 0 is rejected even when it is after now', () => {
    expect(check(-10, 30, { now: -20 })).toBe(false);
  });
});