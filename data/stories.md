## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## about cafeteria - timing
* about_policy
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_policy
* cafeteria_timing
- utter_cafeteria_timing

## about cafeteria - payments
* about_policy
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_policy
* cafeteria_payments
- utter_cafeteria_payments

## about cafeteria - guests
* about_policy
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_policy
* cafeteria_guest
- utter_cafeteria_guests

## about cafeteria - visiting employees
* about_policy
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_policy
* cafeteria_visiting_employee
- utter_cafeteria_visiting_employee

## about cafeteria - Coupons
* about_policy
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_policy
* cafeteria_coupons
- utter_cafeteria_coupons

## about cafeteria - temp-staff
* about_policy
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_policy
* cafeteria_coupons
- utter_cafeteria_coupons

## about cafeteria - temp-staff
* about_policy
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_policy
* cafeteria_temp_employees
- utter_cafeteria_temp_employee

## about payments - cafeteria
* about_payment
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_payments

## cafeteria timing
* about_timing
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_timing

## visitors - temp employee
* about_visitors
- slot{"policy_type":"cafeteria_policy"}
- utter_which_cafeteria_visitors
* cafeteria_temp_employees
- utter_cafeteria_temp_employee

## visitors - guests
* about_visitors
- slot{"policy_type":"cafeteria_policy"}
- utter_which_cafeteria_visitors
* cafeteria_guest
- utter_cafeteria_guests

## visitors - visiting employee
* about_visitors
- slot{"policy_type":"cafeteria_policy"}
- utter_which_cafeteria_visitors
* cafeteria_visiting_employee
- utter_cafeteria_visiting_employee

## visitors - temp employee
* about_visitors{"temporary_staff":"intern"}
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_temp_employee

## visitors - guests
* about_visitors{"guest":"friends"}
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_guests

## visitors - visiting employee
* about_visitors{"visiting_employee":"visiting employees"}
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_visiting_employee

## about cafeteria coupons
* about_coupons
- slot{"policy_type":"cafeteria_policy"}
- utter_cafeteria_coupons

## about food options
* about_food_options
- utter_food_options

## about coupons sad day
* about_coupons
- utter_ask_which_policy
* employee_cafeteria_policy
- action_set_policy_type
- utter_cafeteria_coupons

## about visitors sad day
* about_visitors
- utter_ask_which_policy
* employee_cafeteria_policy
- action_set_policy_type
- utter_which_cafeteria_visitors

## about payment sad day
* about_payment
- utter_ask_which_policy
* employee_cafeteria_policy
- action_set_policy_type
- utter_cafeteria_payments

## about timing sad day
* about_timing
- utter_ask_which_policy
* employee_cafeteria_policy
- action_set_policy_type
- utter_cafeteria_timing