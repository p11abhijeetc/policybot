## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

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
* leave_entitement
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_type
* retail
  - utter_retail_number_of_leaves

## number of leaves - corporate
* leave_entitement
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_type
* corporate
  - utter_corporate_number_of_leaves

## leave entitlement - sick leave
* leave_entitement{"leave_type": "sick"}
  - slot{"leave_type": "sick"}
  - action_set_policy_type
  - utter_sick_leave

## leave entitlement - casual leave
* leave_entitement{"leave_type": "casual"}
  - slot{"leave_type": "casual"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_casual_leave

## leave entitlement - privilege leave retail happy day
* leave_entitement{"leave_type": "privilege", "employee_type": "retail"}
  - slot{"employee_type": "retail"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_privilege_leave_retail

## leave entitlement - privilege leave corporate happy day
* leave_entitement{"leave_type": "privilege", "employee_type": "corporate"}
  - slot{"employee_type": "corporate"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_privilege_leave_corporate

## leave entitlement - privilege leave retail sad day
* leave_entitement{"leave_type": "privilege"}
  - slot{"leave_type": "privilege"}
  - action_set_policy_type
  - slot{"policy_type": "leave_policy"}
  - utter_ask_employee_types
* retail
  - slot{"employee_type": "retail"} 
  - utter_privilege_leave_retail

## leave entitlement - privilege leave corporate sad day
* leave_entitement{"leave_type": "privilege"}
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

## know about leave without pay
* about_leave_types OR leave_entitement OR weekend_counted OR leave_benefits OR seek_approval OR apply_for_benefit OR about_leave
  - slot{"leave_type":"unpaid"}
  - utter_without_pay
  - action_reset_LWP_slot

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

<!--                                               Cafeteria policy stories ----------------------------------------------------------------------------------------  -->
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

<!--      -------------------------------------------------------------------maternity leave stories-----------------------------------  -->

## about policy maternity - apply
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* apply_maternity
- utter_maternity_apply

## about policy maternity - approve
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* approval_process_maternity
- utter_maternity_approve

## about policy maternity - Number of Children
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* number_of_children
- utter_number_of_children

## about policy maternity - Duration
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* maternity_duration
- utter_maternity_duration

## about policy maternity - Child adoption
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* child_adoption
- utter_child_adoption

## about policy maternity - Work from home
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* from_home_working_maternity
- utter_from_home_working_maternity

## about policy maternity - Club
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* club_maternity
- utter_club_maternity

## about policy maternity - Payment
* about_policy{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity
* maternity_payment
- utter_maternity_payment

## about policy maternity - apply
* apply_for_benefit{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_maternity_apply

## about policy maternity - approve
* seek_approval{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_maternity_approve

## about policy maternity - Number of Children
* about_policy{"policy_type":"maternity_leave_policy", "maternity_benefit":"child_number"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"child_number"}
- utter_number_of_children

## about policy maternity - Duration
* about_policy{"policy_type":"maternity_leave_policy", "maternity_benefit":"duration"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"duration"}
- utter_maternity_duration

## about policy maternity - Child adoption
* about_policy{"policy_type":"maternity_leave_policy", "maternity_benefit":"adoption"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"adoption"}
- utter_child_adoption

## about policy maternity - Work from home
* about_policy{"policy_type":"maternity_leave_policy", "maternity_benefit":"work_from_home"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"work_from_home"}
- utter_from_home_working_maternity

## about policy maternity - Club
* about_policy{"policy_type":"maternity_leave_policy", "leave_benefit":"club"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"leave_benefit":"club"}
- utter_club_maternity

## about policy maternity - Payment
* about_payment{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_maternity_payment

## about policy maternity - apply
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* apply_maternity
- utter_maternity_apply

## about policy maternity - approve
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* approval_process_maternity
- utter_maternity_approve

## about policy maternity - Number of Children
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* number_of_children
- utter_number_of_children

## about policy maternity - Duration
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* maternity_duration
- utter_maternity_duration

## about policy maternity - Child adoption
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* child_adoption
- utter_child_adoption

## about policy maternity - Work from home
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* from_home_working_maternity
- utter_from_home_working_maternity

## about policy maternity - Club
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* club_maternity
- utter_club_maternity

## about policy maternity - Payment
* patental_leave_benefits{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_about_maternity_benefits
* maternity_payment
- utter_maternity_payment

## about policy maternity - Number of Children
* patental_leave_benefits{"policy_type":"maternity_leave_policy", "maternity_benefit":"child_number"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"child_number"}
- utter_number_of_children

## about policy maternity - Duration
* patental_leave_benefits{"policy_type":"maternity_leave_policy", "maternity_benefit":"duration"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"duration"}
- utter_maternity_duration

## about policy maternity - Child adoption
* patental_leave_benefits{"policy_type":"maternity_leave_policy", "maternity_benefit":"adoption"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"adoption"}
- utter_child_adoption

## about policy maternity - Work from home
* patental_leave_benefits{"policy_type":"maternity_leave_policy", "maternity_benefit":"work_from_home"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"maternity_benefit":"work_from_home"}
- utter_from_home_working_maternity

## about policy maternity - Club
* patental_leave_benefits{"policy_type":"maternity_leave_policy", "leave_benefit":"club"}
- slot{"policy_type":"maternity_leave_policy"}
- slot{"leave_benefit":"club"}
- utter_club_maternity

## maternity counted as leave
* parental_leave_counted{"policy_type":"maternity_leave_policy"}
- slot{"policy_type":"maternity_leave_policy"}
- utter_maternity_not_counted

<!-- -------------------------------------------------------------------------Paternity policy stories-----------------------------------------------------  -->

## paternity counted as leave
* parental_leave_counted{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_counted_paternity

## about policy paternity - apply
* about_policy{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* apply_paternity
- utter_apply_paternity

## about policy paternity - approve
* about_policy{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* approval_process_paternity
- utter_approval_process_paternity

## about policy paternity - Number of Children
* about_policy{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* number_of_children
- utter_number_of_children_paternity

## about policy paternity - Duration
* about_policy{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* paternity_duration
- utter_paternity_duration

## about policy paternity - adoption
* about_policy{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* child_adoption
- utter_child_adoption_paternity

## about policy paternity - apply
* apply_for_benefit{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_apply_paternity

## about policy paternity - approve
* seek_approval{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_approval_process_paternity

## about policy paternity - Number of Children
* about_policy{"policy_type":"paternity_leave_policy", "maternity_benefit":"child_number"}
- slot{"policy_type":"paternity_leave_policy"}
- slot{"maternity_benefit":"child_number"}
- utter_number_of_children_paternity

## about policy paternity - Duration
* about_policy{"policy_type":"paternity_leave_policy", "maternity_benefit":"duration"}
- slot{"policy_type":"paternity_leave_policy"}
- slot{"maternity_benefit":"duration"}
- utter_paternity_duration

## about policy paternity - adoption
* about_policy{"policy_type":"paternity_leave_policy", "maternity_benefit":"adoption"}
- slot{"policy_type":"paternity_leave_policy"}
- slot{"maternity_benefit":"adoption"}
- utter_child_adoption_paternity

## about policy paternity - apply
* patental_leave_benefits{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* apply_paternity
- utter_apply_paternity

## about policy paternity - approve
* patental_leave_benefits{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* approval_process_paternity
- utter_approval_process_paternity

## about policy paternity - Number of Children
* patental_leave_benefits{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* number_of_children
- utter_number_of_children_paternity

## about policy paternity - Duration
* patental_leave_benefits{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* paternity_duration
- utter_paternity_duration

## about policy paternity - adoption
* patental_leave_benefits{"policy_type":"paternity_leave_policy"}
- slot{"policy_type":"paternity_leave_policy"}
- utter_about_paternity
* child_adoption
- utter_child_adoption_paternity

## about policy paternity - Number of Children
* patental_leave_benefits{"policy_type":"paternity_leave_policy", "maternity_benefit":"child_number"}
- slot{"policy_type":"paternity_leave_policy"}
- slot{"maternity_benefit":"child_number"}
- utter_number_of_children_paternity

## about policy paternity - Duration
* patental_leave_benefits{"policy_type":"paternity_leave_policy", "maternity_benefit":"duration"}
- slot{"policy_type":"paternity_leave_policy"}
- slot{"maternity_benefit":"duration"}
- utter_paternity_duration

## about policy paternity - adoption
* patental_leave_benefits{"policy_type":"paternity_leave_policy", "maternity_benefit":"adoption"}
- slot{"policy_type":"paternity_leave_policy"}
- slot{"maternity_benefit":"adoption"}
- utter_child_adoption_paternity