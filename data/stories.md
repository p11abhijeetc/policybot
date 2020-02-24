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
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_about_leave_policy
* apply_for_benefit
  - slot{"policy_type":"leave_policy"}
  - utter_leave_apply

## about sick leave
* about_leave{"leave_type":"sick"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_sick

## about  casual leave
* about_leave{"leave_type": "casual"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_casual

## about privilege leaves - retail
* about_leave{"leave_type": "privilege"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_type
* retail
  - utter_privilege_retail

## about privilege leaves - corporate
* about_leave{"leave_type": "privilege"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_type
* corporate
  - utter_privilege_corporate

## number of leaves - retial
* numberof_leave
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_type
* retail
  - utter_retail_number_of_leaves

## number of leaves - corporate
* numberof_leave
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_type
* corporate
  - utter_corporate_number_of_leaves

## leave entitlement - sick leave
* numberof_leave{"leave_type": "sick"}
  - slot{"leave_type": "sick"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_sick_leave

## leave entitlement - casual leave
* numberof_leave{"leave_type": "casual"}
  - slot{"leave_type": "casual"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_casual_leave

## leave entitlement - privilege leave retail happy day
* numberof_leave{"leave_type": "privilege", "employee_type": "retail"}
  - slot{"employee_type": "retail"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_privilege_leave_retail

## leave entitlement - privilege leave corporate happy day
* numberof_leave{"leave_type": "privilege", "employee_type": "corporate"}
  - slot{"employee_type": "corporate"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_privilege_leave_corporate

## leave entitlement - privilege leave retail sad day
* numberof_leave{"leave_type": "privilege"}
  - slot{"leave_type": "privilege"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_types
* retail
  - slot{"employee_type": "retail"} 
  - utter_privilege_leave_retail

## leave entitlement - privilege leave corporate sad day
* numberof_leave{"leave_type": "privilege"}
  - slot{"leave_type": "privilege"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_types
* corporate
  - slot{"employee_type": "corporate"} 
  - utter_privilege_leave_corporate

## know about sick leave
* about_leave_types
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_different_leaves
* sick
  - utter_sick

## know about casual leave
* about_leave_types
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_different_leaves
* casual
  - utter_casual

## know about leave without pay
* about_leave_types
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_different_leaves
* without_pay
  - utter_without_pay

## know about maternity leave
* about_leave_types
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_different_leaves
* maternity
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity

## know about paternity leave
* about_leave_types
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_different_leaves
* paternity
  - utter_paternity

## know about privilege leave - corporate
* about_leave_types
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_different_leaves
* privilege
  - utter_ask_employee_types
* corporate
  - utter_privilege_corporate

## know about privilege leave - retail
* about_leave_types
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_different_leaves
* privilege
  - utter_ask_employee_types
* retail
  - utter_privilege_retail

## know about leave benefits- approval
* leave_benefits
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_which_benefit
* approve_leave
  - utter_approve

## know about leave benefits- club
* leave_benefits
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_which_benefit
* club_leave
  - utter_club

## know about leave benefits- carry forward
* leave_benefits
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_which_benefit
* leave_carry_forward
  - utter_carry_forward

## know about leave benefits- proration
* leave_benefits
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_which_benefit
* leave_proration
  - utter_proration

## know about leave benefits- encash
* leave_benefits
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_which_benefit
* encash_leave
  - utter_encash

## know about leave benefits- weekends counted
* leave_benefits
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_which_benefit
* weekend_counted
  - utter_weekends_counted

## know about leave benefits- apply
* leave_benefits
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_which_benefit
* apply_leave
  - utter_leave_apply

## know about leave benefits- apply
* apply_for_benefit
  - slot{"policy_type": "leave_policy"}
  - utter_leave_apply

## know about leave benefits- weekend counted
* weekend_counted
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_weekends_counted

## know about leave benefits- approve
* leave_benefits{"leave_benefit": "approval"}
  - slot{"leave_benefit": "approval"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_approve

## know about leave benefits- approve
* seek_approval
  - slot{"policy_type": "leave_policy"}
  - utter_approve

## know about leave benefits- club
* leave_benefits{"leave_benefit": "club"}
  - slot{"leave_benefit": "club"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_club

## know about leave benefits- encash
* leave_benefits{"leave_benefit": "encash"}
  - slot{"leave_benefit": "encash"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_encash

## know about leave benefits- carry forward
* leave_benefits{"leave_benefit": "carry_forward"}
  - slot{"leave_benefit": "carry_forward"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_carry_forward

## know about leave benefits- proration
* leave_benefits{"leave_benefit": "proration"}
  - slot{"leave_benefit": "proration"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_proration

## apply for maternity leave
* apply_for_benefit
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_apply

## apply for maternity leave -with mat leave policy type
* apply_for_benefit{"policy_type": "maternity_leave_policy"}
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_apply

## maternity counted as regular leave
* maternity_counted
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_not_counted

## know about maternity benefits - apply
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* apply_maternity
  - utter_maternity_apply

## know about maternity benefits - approve
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* approval_process_maternity
  - utter_maternity_approve

## know about maternity benefits - number_of_children
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* number_of_children
  - utter_number_of_children

## know about maternity benefits - duration
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* maternity_duration
  - utter_maternity_duration

## know about maternity benefits - child_adoption
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* child_adoption
  - utter_child_adoption

## know about maternity benefits - work from home
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* from_home_working_maternity
  - utter_from_home_working_maternity

## know about maternity benefits - club with other leaves
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* club_maternity
  - slot{"leave_benefit": "club"}
  - utter_club_maternity

## know about maternity benefits - payment during maternity
* about_maternity_benefits
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_about_maternity_benefits
* maternity_payment
  - utter_maternity_payment

## know about maternity benefits - club with other leaves happy day
* about_maternity_benefits{"leave_benefit":"club"}
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - slot{"leave_benefit":"club"}
  - utter_club_maternity

## know about maternity benefits - work from home happy day
* about_maternity_benefits{"maternity_benefit":"work_from_home"}
  - slot{"maternity_benefit":"work_from_home"}
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_from_home_working_maternity

## know about maternity benefits - child adoption happy day
* about_maternity_benefits{"maternity_benefit":"adoption"}
  - slot{"maternity_benefit":"adoption"}
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_child_adoption

## know about maternity benefits - duration happy day
* about_maternity_benefits{"maternity_benefit":"duration"}
  - slot{"maternity_benefit":"duration"}
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_duration

## know about maternity benefits - number_of_children happy day
* about_maternity_benefits{"maternity_benefit":"child_number"}
  - slot{"maternity_benefit":"child_number"}
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_number_of_children

## know about maternity benefits - approval happy day
* about_maternity_benefits{"leave_benefit":"approval"}
  - slot{"leave_benefit":"approval"}
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_approve

## know about maternity benefits - approval happy day
* seek_approval
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_approve

## know about maternity benefits - approval with ploicy type happy day
* seek_approval{"policy_type": "maternity_leave_policy"}
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_approve

## know about maternity benefits - payment during maternity happy day
* about_maternity_benefits{"maternity_benefit":"payment"}
  - slot{"maternity_benefit":"payment"}
  - action_set_policy_type
  - slot{"policy_type": "maternity_leave_policy"}
  - utter_maternity_payment

<!-- ---------------------------------------------------------------------------Paternity Leave Stories-------------------------------------             -->
## about paternity leave - apply
* apply_for_benefit
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_apply_paternity

## about paternity leave - apply with policy type
* apply_for_benefit{"policy_type": "paternity_leave_policy"}
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_apply_paternity

## about paternity leave - approval
* seek_approval
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_approval_process_paternity

## about paternity leave - approval with policy type
* seek_approval{"policy_type": "paternity_leave_policy"}
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_approval_process_paternity

## paternity countet
* paternity_counted
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_counted_paternity

## about paternity benefit sad day - apply
* paternity_benefit
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_about_paternity
* apply_paternity
  - utter_apply_paternity

## about paternity benefit sad day - approve
* paternity_benefit
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_about_paternity
* approval_process_paternity
  - utter_approval_process_paternity

## about paternity benefit sad day - number of children
* paternity_benefit
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_about_paternity
* number_of_children
  - utter_number_of_children_paternity

## about paternity benefit sad day - adoption
* paternity_benefit
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_about_paternity
* child_adoption
  - utter_child_adoption_paternity

## about paternity benefit sad day - duration
* paternity_benefit
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_about_paternity
* paternity_duration
  - utter_paternity_duration

## about paternity benefit happy day - number of children
* paternity_benefit{"maternity_benefit": "child_number"}
  - slot{"maternity_benefit": "child_number"}
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_number_of_children_paternity

## about paternity benefit sad day - adoption
* paternity_benefit{"maternity_benefit": "adoption"}
  - slot{"maternity_benefit": "adoption"}
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_child_adoption_paternity

## about paternity benefit sad day - duration
* paternity_benefit{"maternity_benefit": "duration"}
  - slot{"maternity_benefit": "duration"}
  - action_set_policy_type
  - slot{"policy_type": "paternity_leave_policy"}
  - utter_paternity_duration
