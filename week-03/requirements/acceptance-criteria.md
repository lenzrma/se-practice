# Acceptance criteria — three selected stories

Assumptions first, then the criteria. Each block names the story it belongs to.

---

## Assumptions

- **Overlap:** a booking that ends exactly when another begins is allowed under R3, because a true overlap requires the two bookings to share an instant of room occupancy, and a booking that ends at 14:00 does not occupy the room at 14:00 while the next one starts.
- **Duration:** a booking of exactly two hours is allowed under R2, because "at most two hours" is an inclusive upper bound, not a strict one.
- Blocking a room (R4) does not retroactively cancel bookings that already exist for it; it only stops new bookings from being made against a blocked room.

---

## US-02 — Book room

### AC-01
- **Given** the room is free for the requested slot and the slot starts in the future
- **When** the Student submits a booking for up to two hours
- **Then** the booking is created and the room is marked reserved for that slot

### AC-02
- **Given** the requested slot starts in the past
- **When** the Student submits the booking
- **Then** the system rejects it with a message that a booking must start in the future (R1)

### AC-03
- **Given** the requested duration is more than two hours
- **When** the Student submits the booking
- **Then** the system rejects it as exceeding the maximum duration (R2)

### AC-04
- **Given** another confirmed booking already occupies part of the same room and slot
- **When** the Student submits an overlapping booking
- **Then** the system rejects it as a conflict with an existing booking (R3)

### AC-05
- **Given** the room is free and the requested slot is exactly two hours long
- **When** the Student submits the booking
- **Then** the booking is accepted, because exactly two hours is not "more than" the limit (boundary case for R2)

---

## US-03 — Cancel booking

### AC-06
- **Given** the Student has an active booking that has not started yet
- **When** the Student cancels it
- **Then** the booking is removed and the room becomes available again for that slot

### AC-07
- **Given** the booking belongs to a different student
- **When** a Student attempts to cancel it
- **Then** the system rejects the request as unauthorized

### AC-08
- **Given** the booking has already been cancelled
- **When** the Student attempts to cancel it again
- **Then** the system rejects the request as invalid, since there is nothing left to cancel

### AC-09
- **Given** the booking's start time has already passed
- **When** the Student attempts to cancel it
- **Then** the system rejects the cancellation, because a booking that already started cannot be released

---

## US-04 — Block or unblock room

### AC-10
- **Given** the room is currently available and has no rule blocking it
- **When** the Administrator blocks the room
- **Then** the room is marked blocked and stops appearing as bookable (R4)

### AC-11
- **Given** the room is blocked
- **When** a Student attempts to book it
- **Then** the system rejects the booking, because a blocked room cannot be booked (R4)

### AC-12
- **Given** the room is currently blocked
- **When** the Administrator unblocks it
- **Then** the room becomes available for booking again

### AC-13
- **Given** the room already has confirmed future bookings
- **When** the Administrator blocks the room
- **Then** those existing bookings stay valid and are not cancelled by the block
