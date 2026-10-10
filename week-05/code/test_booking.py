import unittest
from booking import can_book

class BookingTests(unittest.TestCase):

    def test_end_of_day_inclusive(self):
        # AC1: end at 1440 (midnight of next day) is allowed
        self.assertTrue(can_book(1380, 1440, 540, False, []))

    def test_out_of_bounds_end(self):
        # AC1: end > 1440 should be rejected
        self.assertFalse(can_book(1380, 1441, 540, False, []))

    def test_start_one_min_after_now(self):
        # AC1: start > now (541 > 540)
        self.assertTrue(can_book(541, 571, 540, False, []))

    def test_start_in_past(self):
        # AC1: start in past (500 < 540)
        self.assertFalse(can_book(500, 530, 540, False, []))

    def test_starts_now(self):
        # AC1: start == now should be rejected
        self.assertFalse(can_book(540, 600, 540, False, []))

    def test_exact_2_hours(self):
        # AC2: exactly 120 minutes is allowed (end - start == 120)
        self.assertTrue(can_book(600, 720, 540, False, []))

    def test_over_2_hours(self):
        # AC2: 121 minutes should be rejected
        self.assertFalse(can_book(600, 721, 540, False, []))

    def test_zero_length(self):
        # AC1: start >= end should be rejected
        self.assertFalse(can_book(600, 600, 540, False, []))

    def test_reversed_times(self):
        # AC1: start > end should be rejected
        self.assertFalse(can_book(660, 600, 540, False, []))

    def test_blocked(self):
        # AC3: blocked room accepts nothing
        self.assertFalse(can_book(600, 660, 540, True, []))

    def test_overlap_left(self):
        # AC4: overlaps left
        existing = [(600, 660)]
        self.assertFalse(can_book(570, 630, 540, False, existing))

    def test_overlap_encloses(self):
        # AC4: encloses existing
        existing = [(600, 660)]
        self.assertFalse(can_book(570, 690, 540, False, existing))

    def test_overlap_identical(self):
        # AC4: identical interval
        existing = [(600, 660)]
        self.assertFalse(can_book(600, 660, 540, False, existing))

    def test_touching_left_allowed(self):
        # AC4: touching endpoints are allowed (ends at existing start)
        existing = [(600, 660)]
        self.assertTrue(can_book(570, 600, 540, False, existing))

    def test_touching_right_allowed(self):
        # AC4: touching endpoints are allowed (starts at existing end)
        existing = [(600, 660)]
        self.assertTrue(can_book(660, 720, 540, False, existing))

    def test_multiple_existing_overlap_second(self):
        # AC4: crosses second interval in list
        existing = [(600, 660), (700, 760)]
        self.assertFalse(can_book(720, 780, 540, False, existing))

    def test_unsorted_existing(self):
        # AC4: checks unsorted existing list correctly
        existing = [(900, 960), (600, 660)]
        self.assertFalse(can_book(610, 650, 540, False, existing))

    def test_window_between_three(self):
        # AC4: window between three existing bookings
        existing = [(600, 660), (700, 760), (800, 860)]
        self.assertTrue(can_book(760, 800, 540, False, existing))

    def test_immutability(self):
        # AC5: inputs are left unchanged after multiple calls
        existing = [(900, 960), (600, 660), (700, 760)]
        existing_copy = [item for item in existing]
        can_book(780, 840, 540, False, existing)
        can_book(610, 650, 540, False, existing)
        self.assertEqual(existing, existing_copy)

    def test_table_overlap(self):
        self.assertIs(can_book(630, 690, 540, False, [(600, 660)]), False)

    def test_table_blocked(self):
        self.assertIs(can_book(660, 720, 540, True, [(600, 660)]), False)

    def test_table_exact_2_hours(self):
        self.assertIs(can_book(720, 840, 540, False, [(600, 660)]), True)

    def test_table_over_2_hours(self):
        self.assertIs(can_book(720, 841, 540, False, [(600, 660)]), False)

    def test_table_starts_now(self):
        self.assertIs(can_book(540, 570, 540, False, [(600, 660)]), False)

if __name__ == '__main__':
    unittest.main()