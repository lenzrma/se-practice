import unittest
from booking import can_book


class BookingTests(unittest.TestCase):
    # T1: touching endpoints
    def test_touching_endpoint_allowed(self):
        self.assertTrue(can_book(660, 720, 540, False, [(600, 660)]))

    # T2: overlap
    def test_overlap_rejected(self):
        self.assertFalse(can_book(630, 690, 540, False, [(600, 660)]))

    # T3: blocked
    def test_blocked_room_rejected(self):
        self.assertFalse(can_book(660, 720, 540, True, [(600, 660)]))

    # T4: exactly 120
    def test_exactly_120_minutes_allowed(self):
        self.assertTrue(can_book(720, 840, 540, False, [(600, 660)]))

    # T5: 121
    def test_over_120_minutes_rejected(self):
        self.assertFalse(can_book(720, 841, 540, False, [(600, 660)]))

    # T6: starts now
    def test_starts_now_rejected(self):
        self.assertFalse(can_book(540, 570, 540, False, [(600, 660)]))

    # T7: reversed
    def test_reversed_times_rejected(self):
        self.assertFalse(can_book(720, 660, 540, False, [(600, 660)]))

    # T8: ends at midnight
    def test_ends_at_midnight_allowed(self):
        self.assertTrue(can_book(1380, 1440, 540, False, [(600, 660)]))

    # T9: past midnight
    def test_past_midnight_rejected(self):
        self.assertFalse(can_book(1380, 1441, 540, False, [(600, 660)]))

    # T10: second booking
    def test_multiple_existing_bookings_overlap(self):
        self.assertFalse(can_book(720, 780, 540, False, [(600, 660), (700, 760)]))

    # T11: same check twice
    def test_same_check_twice_idempotent(self):
        r1 = can_book(660, 720, 540, False, [(600, 660)])
        r2 = can_book(660, 720, 540, False, [(600, 660)])
        self.assertTrue(r1 and r2)

    # AC5: inputs unchanged
    def test_existing_list_not_mutated(self):
        existing = [(900, 960), (600, 660)]
        copy = list(existing)
        can_book(660, 720, 540, False, existing)
        self.assertEqual(existing, copy)

    # AC1
    def test_zero_length_rejected(self):
        self.assertFalse(can_book(700, 700, 540, False, []))

    def test_negative_start_rejected(self):
        self.assertFalse(can_book(-30, 30, 0, False, []))

    def test_start_one_minute_after_now_allowed(self):
        self.assertTrue(can_book(541, 571, 540, False, []))

    def test_start_in_past_rejected(self):
        self.assertFalse(can_book(500, 530, 540, False, []))

    def test_now_zero_start_zero_rejected(self):
        self.assertFalse(can_book(0, 60, 0, False, []))

    def test_now_zero_start_one_allowed(self):
        self.assertTrue(can_book(1, 61, 0, False, []))

    # AC4
    def test_overlap_over_start_rejected(self):
        self.assertFalse(can_book(570, 630, 540, False, [(600, 660)]))

    def test_inside_existing_rejected(self):
        self.assertFalse(can_book(615, 645, 540, False, [(600, 660)]))

    def test_contains_existing_rejected(self):
        self.assertFalse(can_book(570, 690, 540, False, [(600, 660)]))

    def test_identical_to_existing_rejected(self):
        self.assertFalse(can_book(600, 660, 540, False, [(600, 660)]))

    def test_ends_at_existing_start_allowed(self):
        self.assertTrue(can_book(570, 600, 540, False, [(600, 660)]))

    def test_unsorted_bookings_overlap_rejected(self):
        self.assertFalse(can_book(610, 650, 540, False, [(900, 960), (600, 660)]))

    def test_fits_exactly_between_two_allowed(self):
        self.assertTrue(can_book(660, 720, 540, False, [(600, 660), (720, 780)]))

    def test_no_bookings_allowed(self):
        self.assertTrue(can_book(600, 660, 540, False, []))


if __name__ == "__main__":
    unittest.main()