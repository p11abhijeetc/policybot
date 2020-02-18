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

## ask and apply
* about_leave
  - utter_about_leave_policy
* apply_leave
  - utter_leave_apply

## number of leaves - retial
* numberof_leave
  - utter_ask_employee_type
* retail
  - utter_retail_number_of_leaves

## number of leaves - corporate
* numberof_leave
  - utter_ask_employee_type
* corporate
  - utter_corporate_number_of_leaves

## know about sick leave
* about_leave_types
  - utter_different_leaves
* sick
  - utter_sick

## know about casual leave
* about_leave_types
  - utter_different_leaves
* casual
  - utter_casual

## know about leave without pay
* about_leave_types
  - utter_different_leaves
* without_pay
  - utter_without_pay

## know about maternity leave
* about_leave_types
  - utter_different_leaves
* maternity
  - utter_maternity

## know about paternity leave
* about_leave_types
  - utter_different_leaves
* paternity
  - utter_paternity

## know about privilege leave - corporate
* about_leave_types
  - utter_different_leaves
* privilege
  - utter_ask_employee_types
* corporate
  - utter_privilege_corporate

## know about privilege leave - retail
* about_leave_types
  - utter_different_leaves
* privilege
  - utter_ask_employee_types
* retail
  - utter_privilege_retail

## know about leave benefits- approval
* leave_benefits
  - utter_which_benefit
* approve_leave
  - utter_approve

## know about leave benefits- club
* leave_benefits
  - utter_which_benefit
* club_leave
  - utter_club

## know about leave benefits- carry forward
* leave_benefits
  - utter_which_benefit
* leave_carry_forward
  - utter_carry_forward

## know about leave benefits- proration
* leave_benefits
  - utter_which_benefit
* leave_proration
  - utter_proration

## know about leave benefits- encash
* leave_benefits
  - utter_which_benefit
* encash_leave
  - utter_encash

## know about leave benefits- weekends counted
* leave_benefits
  - utter_which_benefit
* weekend_counted
  - utter_weekends_counted

## know about leave benefits- apply
* leave_benefits
  - utter_which_benefit
* apply_leave
  - utter_leave_apply

## know about leave benefits- apply
* apply_leave
  - utter_leave_apply

## know about leave benefits- weekend counted
* weekend_counted
  - utter_weekends_counted

## know about leave benefits- approve
* leave_benefits{"leave_benefit": "approval"}
  - slot{"leave_benefit": "approval"}
  - utter_approve

## know about leave benefits- club
* leave_benefits{"leave_benefit": "club"}
  - slot{"leave_benefit": "club"}
  - utter_club

## know about leave benefits- encash
* leave_benefits{"leave_benefit": "encash"}
  - slot{"leave_benefit": "encash"}
  - utter_encash

## know about leave benefits- carry forward
* leave_benefits{"leave_benefit": "carry_forward"}
  - slot{"leave_benefit": "carry_forward"}
  - utter_carry_forward

## know about leave benefits- proration
* leave_benefits{"leave_benefit": "proration"}
  - slot{"leave_benefit": "proration"}
  - utter_proration

