## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent: about_leave
- Is there a leave policy?
- Does the company have a leave policy?
- What is leave policy?
- What is company leave policy?
- Please tell me about leave policy?
- And what about leave policy?
- And leave policy?
- May i know about leave policy?
- Please tell me about [sick](leave_type:sick) leaves
- Please tell me more about [casual](leave_type:casual) leaves
- And [privilege](leave_type:privilege) leaves?
- What about [sick](leave_type:sick) leave?
- May i know about [SL](leave_type:sick) leave?
- Please tell me about [CL](leave_type:casual)
- May i know about [PL](leave_type:privilege)
- Please tell me more about [earned](leave_type:privilege) leaves
- Explain about leave
- leave policy
- leave
- Can you tell me about [leave without pay](leave_type:unpaid)
- And what about [LWP](leave_type:unpaid)
- Please tell me about [lwp](leave_type:unpaid)

## intent: apply_for_benefit
- I want to apply for leave
- How to apply
- How can i apply
- What is the process to apply
- I want to apply
- I need leave
- How can i apply for leave
- How to apply leave
- Apply leave
- how can i get leaves?
- I want apply for [sick](leave_type:sick) leave
- I want to apply [casual](leave_type:casual) leave
- I want to apply for [earned](leave_type:privilege) leave
- How can i apply for [maternity](policy_type:maternity_leave_policy)?
- How to apply for [maternity](policy_type:maternity_leave_policy)?
- How can i get [maternity](policy_type:maternity_leave_policy) leave?
- How to apply for [maternity](policy_type:maternity_leave_policy) leave?
- What is the process for applying for [maternity](policy_type:maternity_leave_policy) leave?
- What is the procedure to apply for [maternity](policy_type:maternity_leave_policy) leave?
- What is the notice period for my [maternity](policy_type:maternity_leave_policy) leave?
- I want to apply for [mat](policy_type:maternity_leave_policy) leave
- how to apply for [paternity](policy_type:paternity_leave_policy) leave?
- how can i apply [pat](policy_type:paternity_leave_policy) leave?
- how can i apply for [sick](leave_type:sick) leave?
- how to apply for [paternity](policy_type:paternity_leave_policy) leave?
- How can i apply for [patternity](policy_type:paternity_leave_policy) leave?
- can i get [paternity](policy_type:paternity_leave_policy) leave?
- What is the process for applying for [pat](policy_type:paternity_leave_policy) leave?
- What is the process for applying for [paternity](policy_type:paternity_leave_policy) leave?
- Is there a separate process to apply for [LWP](leave_type:unpaid)

## intent: seek_approval
- who will [approve](leave_benefit:approval) my [maternity](policy_type:maternity_leave_policy) leave?
- How will my [maternity](policy_type:maternity_leave_policy) leave be [approved](leave_benefit:approval)?
- What is the [approval](leave_benefit:approval) process for [maternity](policy_type:maternity_leave_policy) leave?
- I have an urgent requirement of leaves. Do i need [approval](leave_benefit:approval)?
- I have an emergency. Can i go on leave without [approval](leave_benefit:approval)?
- Is [approval](leave_benefit:approval) needed for going on leave?
- Do i need manager [approval](leave_benefit:approval) before going on leave?
- Is manager [approval](leave_benefit:approval) required?
- Does my manager need to [approve](leave_benefit:approval) my leaves?
- Is approval needed for [LWP](leave_type:unpaid)
- Who will approve if i want to go on a long [unpaid leave](leave_type:witout_pay)
- Is approval needed?
- How to get an approval?
- What is the approval process?
- Is approval mandatory?
- How can i get an approval?
- I want to go on maternity leave?
- How to apply for paternity leave?
- How can i apply?
- How to apply for pat leave?
- Who will approve my pat leave?
- How can i get my pat leave approved?
- Is prior approval needed?
- Can i go on leave and get it approved later?

## intent: leave_benefits
- I want to know about my leave benefits?
- What leave benefits do i have?
- Can i [club](leave_benefit:club) [sick](leave_type:sick) leave with [PL](leave_type:privilege)
- Is [clubbing](leave_benefit:club) of [CL](leave_type:casual) with [el](leave_type:privilege) allowed 
- Can i [club](leave_benefit:club) my leaves?
- Can i [club](leave_benefit:club) [casual](leave_type:casual) leaves?
- Is [clubbing](leave_benefit:club) allowed?
- Can i [combine](leave_benefit:club) two types of leaves?
- Is [combining](leave_benefit:club) leave types allowed?
- Can i [club](leave_benefit:club) [casual](leave_type:casual) leaves?
- Is [clubbing](leave_benefit:club) of [sick](leave_type:sick) leaves allowed?
- Can leaves be [clubbed](leave_benefit:club)
- Can i [club](leave_benefit:club) [sick](leave_type:sick) leaves with [casual](leave_type:casual) leaves? 
- Can i [mix and match](leave_benefit:club) leave types?
- Are the leaves [carried forward](leave_benefit:carry_forward)
- Will my leaves get [lapsed](leave_benefit:carry_forward)
- Is is allowed to [carry forward](leave_benefit:carry_forward) leaves?
- Will my leaves get [lapsed](leave_benefit:carry_forward) if i don't use them?
- Will my leaves get [lapse](leave_benefit:carry_forward)
- Will leaves be [prorated](leave_benefit:proration)?
- Is there any kind of [proration](leave_benefit:proration)?
- Is there leave [proration](leave_benefit:proration)?
- Will my leaves be on [pro rata basis](leave_benefit:proration)
- Can i [encash](leave_benefit:encash) my leaves?
- Are leaves [encashable](leave_benefit:encash)?
- Is there an option to [encash](leave_benefit:encash) my leaves?
- Is leave [encashment](leave_benefit:encash) possible?
- How are leave [encashment](leave_benefit:encash) calculated?
- what is leave [encashment](leave_benefit:encash) policy?

## intent: weekend_counted
- Will the weekends falling during my holiday counted?
- Holiday during my leave will be consideres as leave?
- Will the weekends also be counted?
- If i combine a holiday with my leaves, will it be counted?
- Are weekends considered as leave?
- Will the weekends be considered as leave?
- weekend_counted
- are off days counted in leaves?
- If i am on leave on a holiday, will that be counted as a leave?
- If i am on leave on an off day, will that be counted as a leave?

## intent: about_leave_types
- What are the types of leaves
- How many differnt kinds of leaves
- What all leaves are there?
- What the the different kinds of leaves?
- What are the different types of leaves?
- How many kinds of leaves are there?
- Are there different kinds of leaves?
- Tell me about the types of leaves?
- Can i know different leave types?

## intent: leave_entitement
- Can i get leave
- Can i get [sick](leave_type:sick) leave?
- I am [not well](leave_type:sick). can i take the day off?
- I have [fever](leave_type:sick). May i take leave?
- I am [not feeling well](leave_type:sick) and wanted to take leave today?
- How many [sick](leave_type:sick) leaves can i take?
- Is there any limit on the number of [sick] leave
- How many leaves do you have?
- What is my total leaves?
- What is the total number leaves?
- What is my leave entitlement?
- Will i need [medical certificate](leave_benefit:medical_certificate) for [sick](leave_type:sick) leaves
- Do i have to show any [doctor certificate](leave_benefit:medical_certificate) for going on leave?
- I am required to produce any [certificate from a doctor](leave_benefit:medical_certificate) for [sick](leave_type:sick) leaves 
- What is my [sick](leave_type:sick) leave entitlement?
- How many [sick](leave_type:sick) leaves do i have?
- How many [casual](leave_type:casual) leaves can i get?
- Can i take leave for more than 5 days?
- Can i get [sick](leave_type:sick) leave?
- How many leaves can i take in one go?
- How many [privilege](leave_type:privilege) leaves can i take?
- And [casual](leave_type:casual) leaves
- what about [sick](leave_type:sick) leaves
- I am [retail](employee_type:retail) employee. How many [privilege](leave_type:privilege) leaves can i take?
- I am [corporate](employee_type:corporate) employee. How many [privilege](leave_type:privilege) leaves can i take?
- I work in the [store](employee_type:retail). How many [privilege](leave_type:privilege) leaves can i take?
- I work in the [corporate](employee_type:corporate) office. How many [privilege](leave_type:privilege) leaves can i take?
- How many leaves are there?
- Total number of leaves
- How many [sick](leave_type:sick) leaves are there for [retail](employee_type:retail) employees
- How many [casual](leave_type:casual) leaves are there for [corporate](employee_type:corporate) employees
- I am [store](employee_type:retail) staff. How many [privilege](leave_type:privilege) leaves can i take?
- can i take leave for [medical](leave_type:sick) reasons

## intent: about_policy
- Is there a [leave] policy
- Tell me about the [cafeteria](policy_type:cafeteria_policy) facility
- Is there a [cafeteria](policy_type:cafeteria_policy) policy?
- Is there a [cafeteria](policy_type:cafeteria_policy) in office?
- May i know if there are arrangements for [lunch](meal) in office?
- May i know if there are [meal](meal) arrangements in office?
- Is there an option of having [lunch](meal) in office?
- Can i have [lunch](meal) in office?
- Can i have [lunch](meal) in the [cafeteria](policy_type:cafeteria_policy)
- Are there [meal](meal) facilities in office?
- Does the company provide for [cafeteria](policy_type:cafeteria_policy) facility?
- Is there a facility for having [lunch](meal) in office?
- Will employees get [lunch](meal) in office?
- Can i get [lunch] in office?
- What is [cafeteria](policy_type:cafeteria_policy) policy?
- Is there a policy related to [tax saving](policy_type:reimbursement_policy) measures?
- Are there any [tax efficient](policy_type:reimbursement_policy) measures?
- Are there any measures to [save tax](policy_type:reimbursement_policy)
- Does the company promote any measures for [saving tax](policy_type:reimbursement_policy)
- Are there any facilities for [tax planning](policy_type:reimbursement_policy)?
- Can i [plan my tax](policy_type:reimbursement_policy)?
- How can i [save taxes](policy_type:reimbursement_policy)?
- Tell me about income [tax planning](policy_type:reimbursement_policy) measures that the company provides
- May i know about [income tax](policy_type:reimbursement_policy) measures provided to employees?   

## intent: about_timing
- What are the [cafeteria](policy_type:cafeteria_policy) timing?
- Is the [cafeteria](policy_type:cafeteria_policy) open through out the day?
- What are the [cafeteria](policy_type:cafeteria_policy) timings?
- Is the [cafeteria](policy_type:cafeteria_policy) open for the full day?
- Can i get [lunch](meal) in the [cafeteria](policy_type:cafeteria_policy) anytime?
- Can i go for [lunch](meal) now?
- When can i go for [lunch](meal)?
- Can i have [lunch] anytime?
- Is [lunch](meal) served only duirng identified time slots?
- Are there any [lunch](meal) timings?
- When can i have [lunch](meal) at the cafeteria?
- For how long is the [cafeteria](policy_type:cafeteria_policy) open?
- For how long does the [cafeteria](policy_type:cafeteria_policy) remain open?
- What time does the [cafeteria](policy_type:cafeteria_policy) open?
- What time does the [cafeteria](policy_type:cafeteria_policy) close?
- Is the [cafeteria](policy_type:cafeteria_policy) closed now?
- Is the [cafeteria](policy_type:cafeteria_policy) open now?
- Please tell me about the timings?
- may i know about time slots for which the [cafeteria](policy_type:cafeteria_policy) will remain open?
- Can i go to the [cafeteria](policy_type:cafeteria_policy) for food any time?
- Tell me [cafeteria](policy_type:cafeteria_policy) timings.
- May i know [cafeteria](policy_type:cafeteria_policy) timings.

## intent: about_payment
- Do i have to pay for that?
- Will i be charged for [food](meal) in the [cafeteria](policy_type:cafeteria_policy)
- Do i have to pay for the [food](meal) in cafeteria?
- What is the cost of using the [cafeteria](policy_type:cafeteria_policy)
- What are the charges for having [lunch](meal) in the office?
- What are the charges for the [cafeteria](policy_type:cafeteria_policy)?
- What are the charges for having [lunch](meal) in office?
- What are the charges for having [meal](meal) in office?
- What will be the cost of having [lunch](meal)?
- What is the cost of having [meal](meal)?
- What is going to be the cost of having [meal](meal)?
- What is the cost of having [meal](meal) at the [cafeteria](policy_type:cafeteria_policy)?
- Are there any charges?
- What is the cost?
- What are the associated charges?
- What are the associated costs?
- Will i need to pay?
- Will i be charged for this?
- Will my salary be deducted for having lunch in the [cafeteria](policy_type:cafeteria_policy)?
- Will there be any salary deduction for using [cafeteria](policy_type:cafeteria_policy)?
- Will i salary be deducted if i apply for leave?
- Will the company deduct my salary for
- Is [maternity] leave a paid benefit?
- Will there be salary deduction if i 

## intent: about_visitors
- Are [visitors](guest) allowed in [cafeteria](policy_type:cafeteria_policy)?
- Can i take [my friends](guest) to [cafeteria](policy_type:cafeteria_policy)?
- Can i bring [guests](guest) along to the [cafeteria](policy_type:cafeteria_policy)?
- Can i bring a [guest](guest) along for [lunch](meal)?
- Can i bring [guests](guest) to [cafeteria](policy_type:cafeteria_policy)?
- Is bringing [guests](guest) allowed?
- Is bringing [friends](guest) to [cafeteria](policy_type:cafeteria_policy) allowed?
- Can my friend have [lunch](meal) at the company [cafeteria](policy_type:cafeteria_policy)
- Can [visiting employees](visiting_employee) have lunch at office?
- Are [visitors](guest) allowed?
- Can [visitors](guest) have [lunch](meal) at the company [cafeteria](policy_type:cafeteria_policy)?
- Can [staff from other locations](visiting_employee) have lunch at the [cafeteria](policy_type:cafeteria_policy)
- Are [employees from other office](visiting_employee) locations allowed in the [cafeteria](policy_type:cafeteria_policy)
- Can [employees visiting the corporate office](visiting_employee) have [lunch](meal)?
- can i bring [employees from other benetton locations](visiting_employee) have lunch at the [cafeteria](policy_type:cafeteria_policy)
- [Employees from regional offices](visiting_employee) are allowed to have [lunch](meal) at the [cafeteria](policy_type:cafeteria_policy)
- I dont have [food](meal) [regularly](frequency) in the cafeteria(policy_type:cafeteria_policy). Is that allowed?
- Can i have [occassionl](frequency) [meals](meal) in the cafeteria(policy_type:cafeteria_policy)?
- Can i have [once in a while](frequency) [lunch](meal) in cafeteria?
- Can i have [lunch](meal) at the [cafeteria](policy_type:cafeteria_policy) ocassionally?
- I am a [temp](temporary_staff) employee. Can i use the [cafeteria](policy_type:cafeteria_policy)
- I am an [intern](temporary_staff). Am i allowed to have [lunch] in the [cafeteria](policy_type:cafeteria_policy)
- Are [interns](temporary_staff) allowed to use the cafeteria facilities?
- Can [temporary](temporary_staff) staff have [lunch](meal) at the [cafeteria](policy_type:cafeteria_policy)
- I am from Chandigarh office. I have use the [cafeteria](policy_type:cafeteria_policy)
- I am from bangalore. Can i have [lunch](meal) at the [cafeteria](policy_type:cafeteria_policy)
- I am from another office. Can i get [lunch](meal)?

## intent: about_coupons
- How can i get [coupons](voucher)?
- How to purchase [cafeteria](policy_type:cafeteria_policy) [coupons](voucher)?
- Will my [coupons](voucher) get [lapsed](leave_benefit:carry_forward)
- How to get [cafeteria](policy_type:cafeteria_policy)[coupons](voucher)?
- Can i get [cafeteria](policy_type:cafeteria_policy)[coupons](voucher)?
- How to get [vouchers](voucher) for [lunch](meal)
- Can i get [lunch](meal) [vouchers](voucher)
- Can i [carry forward](leave_benefit:carry_forward) meal [vouchers] bought this month to the next month?
- Will my meal [coupons] get [lapsed](leave_benefit:carry_forward)
- Will [coupons](voucher) issued this month be [valid](leave_benefit:carry_forward) next month?
- Is there an [expiry date](leave_benefit:carry_forward) for [cafeteria](policy_type:cafeteria_policy) [coupons](voucher)
- Is there any [validity](leave_benefit:carry_forward) of [coupons](voucher)
- Are [coupons](voucher) [valid](leave_benefit:carry_forward) only for a limited period?
- Can i use [coupons](voucher) issued this month sometime later?
- How can i get the [vouchers](voucher) for the company [cafeteria](policy_type:cafeteria_policy)
- Where can i get [coupons](voucher)

## intent: about_food_options
- Are there other food options in the [cafeteria](policy_type:cafeteria_policy)?
- Does the [cafeteria](policy_type:cafeteria_policy) have snacks counters?
- Can i purchase additional foods in the [cafeteria](policy_type:cafeteria_policy)?
- Are there food joints in the [cafeteria](policy_type:cafeteria_policy)?
- Can i buy snack in the [cafeteria](policy_type:cafeteria_policy)?
- Can i buy my own food in the [cafeteria](policy_type:cafeteria_policy)?
- Are there independent shops in the [cafeteria](policy_type:cafeteria_policy)?
- Are there alternate food options in the [cafeteria](policy_type:cafeteria_policy)?