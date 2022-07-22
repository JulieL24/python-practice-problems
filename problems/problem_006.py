# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# set skydive = True
# if statement to check if > 18, can skydive
# if < 18, needs consent


def can_skydive(age, has_consent_form):
    # skydive = True
    if age >= 18 or has_consent_form is True:
        return True
    if has_consent_form is False or age < 18:
        return False


print(can_skydive(15, True))
print(can_skydive(18, False))
print(can_skydive(17, True))
print(can_skydive(14, False))