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
- What is my leave policy?
- What is our company's leave policy?
- leave
- I want to know about leaves
- I want to know about leave policy?
- Are there privilege(leave_type:privilege) leaves
- Tell me about [sick leaves](leave_type:sick)
- And [casual leave](leave_type:casual)?
- What about [privilege leave](leave_type:privilege)
- I am [retail](employee_type:retail) staff. may i know about [privilege leaves](leave_type:privilege)
- Please tell me about the leave policy
- I want to know about [privilege leaves](leave_type:privilege)
- What about [casual leave](leave_type:casual)?
- And what about [sick leave](leave_type:sick)?

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
- Can i get leaves?
- Can i take leaves?
- I want apply for [sick leave](leave_type:sick)
- I want to apply [casual leave](leave_type:casual)
- I want to apply for [earned leave](leave_type:privilege)
- How can i apply for maternity?
- How to apply for maternity?
- How can i get maternity leave?
- How to apply for maternity leave?
- What is the process for applying for maternity leave?
- What is the procedure to apply for maternity leave?
- What is the notice period for my maternity leave?
- I want to apply for mat leave

## intent: numberof_leave
- How many leaves do you have?
- What is my total leaves?
- What is the total number leaves?
- What is my leave entitlement?
- Will i need [medical certificate](leave_benefit:medical_certificate) for [sick leaves](leave_type:sick)
- Do i have to show any [doctor certificate](leave_benefit:medical_certificate) for going on leave?
- I am required to produce any [certificate from a doctor](leave_benefit:medical_certificate) for [sick leaves](leave_type:sick) 
- What is my [sick leave](leave_type:sick) entitlement?
- How many [sick leaves](leave_type:sick) do i have?
- How many [casual leaves](leave_type:casual) can i get?
- Can i take leave for more than 5 days?
- How many leaves can i take in one go?
- How many [privilege leaves](leave_type:privilege) can i take?
- And [casual leaves](leave_type:casual)
- what about [sick leaves](leave_type:sick)
- I am [retail](employee_type:retail) employee. How many [privilege leaves](leave_type:privilege) can i take?
- I am [corporate](employee_type:corporate) employee. How many [privilege leaves](leave_type:privilege) can i take?
- I work in the [store](employee_type:retail). How many [privilege leaves](leave_type:privilege) can i take?
- I work in the [corporate](employee_type:corporate) office. How many [privilege leaves](leave_type:privilege) can i take?
- How many leaves are there?
- Total number of leaves
- How many [sick leaves](leave_type:sick) are there for [retail](employee_type:retail) employees
- How many [casual leaves](leave_type:casual) are there for [corporate](employee_type:corporate) employees
- I am [store](employee_type:retail) staff. How many [privilege leaves](leave_type:privilege) can i take?
- can i take leave for [medical](leave_type:sick) reasons

## intent: leave_benefits
- I want to know about my leave benefits?
- What leave benefits do i have? 
<!--- Is [approval](leave_benefit:approval) needed for going on leave?
- Do i need manager [approval](leave_benefit:approval) before going on leave?
- Is manager [approval](leave_benefit:approval) required?
- Does my manager need to [approve](leave_benefit:approval)my leaves? -->
- Can i [club](leave_benefit:club) my leaves?
- Can i [club](leave_benefit:club) [casual leaves](leave_type:casual)?
- Is [clubbing](leave_benefit:club) allowed?
- Can i [combine](leave_benefit:club) two types of leaves?
- Is [combining](leave_benefit:club) leave types allowed?
- Can i [club](leave_benefit:club) [casual leaves](leave_type:casual)?
- Is [clubbing](leave_benefit:club) of [sick leaves](leave_type:sick) allowed?
- Can leaves be [clubbed](leave_benefit:club)
- Can i [club](leave_benefit:club)[sick leaves](leave_type:sick) with [casual leaves](leave_type:casual)? 
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
<!--- I have an urgent requirement of leaves. Do i need [approval](leave_benefit:approval)?
- I have an emergency. Can i go on leave without [approval](leave_benefit:approval)? -->
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

## intent: about_maternity
- What is the maternity leave policy?
- Is there a policy for pregnant employees?
- Is there a policy for expecting mothers?
- Is there a policy for leaves during pregnancy?
- Is there any policy for pregnant women?
- Is there a compnay maternity policy?
- Does the company have a maternity leave benefit?
- I want to know about maternity leave?
- And maternity leave?
- what about mat leave?
- what about maternity?
- I want to know about mat leave?

## intent: about_maternity_benefits
- Can i get maternity leave?
- Am i eligible for maternity leave?
- Who is eligible for maternity leave benefit?
- What is the [length](maternity_benefit: duration) of pat leave?
- How [long](maternity_benefit: duration) can be the maternity leave?
- What is the [duration](maternity_benefit:duration) of maternity leave?
- What is the [longest](maternity_benefit: duration) maternity leave i can take
- What is the [maximum length](maternity_benefit:duration) of maternity leave?
- How [many days](maternity_benefit:duration) of maternity
- Can i [extend](maternity_benefit:duration) my maternity leave?
- Can maternity leave be [extended](maternity_benefit:duration)?
- what is the [period](maternity_benefit: duration) of maternity leave?
- what is the [total length](maternity_benefit:duration) of maternity leave?
- will i get maternity leave for child [adoption](maternity_benefit:adoption)
- will i get maternity leave for [adopting](maternity_benefit:adoption) a child?
- Is maternity leave allwoed in case of [adoption](maternity_benefit:adoption)
- Can i get maternity leave if i [adopt](maternity_benefit:adoption)
- For how [many kids](maternity_benefit:child_number) can i take maternity leave?
- For how [many kids](maternity_benefit:child_number) is maternity policy applicable?
- For how [many children](maternity_benefit:child_number) can i get maternity leave?
- For how [many deliveries](maternity_benefit:child_number)
- Is maternity leave applicable only for [first child](maternity_benefit:child_number)?
- Is maternity leave applicable only for [second child](maternity_benefit:child_number)?
- This is my [third child](maternity_benefit:child_number). Will i get leave?
- For how [many childbirths](maternity_benefit:child_number) is maternity leave applicable?
- Will i get a [longer](maternity_benefit: duration) maternity leave for my [first delivery](maternity_benefit:child_number)?
- will i get a leave for my [second delivery](maternity_benefit:child_number)
- will i get a leave for my [first pregnancy](maternity_benefit:child_number)
- Will i get leave for any [number of childbirths](maternity_benefit:child_number)
- Is maternity bennefit applicable to a limited [number of deleveries](maternity_benefit:child_number)
- This is my [second delivery](maternity_benefit:child_number). Will i get maternity leave?
- can i [work from home](maternity_benefit:work_from_home) during pregnancy?
- Am i allowed to [login from home](maternity_benefit:work_from_home) during or after pregnancy? 
- Will i be [paid](maternity_benefit:payment) during maternity?
- will i get my [salary](maternity_benefit:payment) during maternity?
- will my [salary](maternity_benefit: payment) deducted during maternity?
- Am i going to be [unpaid](maternity_benefit:payment) during maternity?
- Is maternity a [paid](maternity_benefit:payment)benefit?
- Is maternity considered leave without pay?
- can i take my maternity leave in [multiple chunks](maternity_benefit:leave_split)
- How much of my maternity leave can i take before childbirth?
- can i [split](maternity_benefit:leave_split) my maternity leave?
- can i take maternity leave in [multiple tranches](maternity_benefit:leave_split)
- can i [club](leave_benefit:club) my maternity leave with other leaves?
- can i [combine](leave_benefit:club) my maternity leave with other leaves?

## intent: maternity_counted
- Will my maternity leave result in deduction of leave balance?
- will maternity leave be counted as regular leave?
- Is maternity counted as leave?
- will maternity be counted as leave?
- Am i going to loose my leaves due to maternity?

## intent: seek_approval
- who will [approve](leave_benefit:approval) my maternity leave?
- How will my maternity leave be [approved](leave_benefit:approval)?
- What is the [approval](leave_benefit:approval) process for maternity leave?
- I have an urgent requirement of leaves. Do i need [approval](leave_benefit:approval)?
- I have an emergency. Can i go on leave without [approval](leave_benefit:approval)?
- Is [approval](leave_benefit:approval) needed for going on leave?
- Do i need manager [approval](leave_benefit:approval) before going on leave?
- Is manager [approval](leave_benefit:approval) required?
- Does my manager need to [approve](leave_benefit:approval)my leaves?
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

<!-- -------------------------------------------------------------------------Paternity Leave -------------------------------------------------------- -->
## intent: about_paternity
- Is there a paternity policy?
- Tell me about paternity policy?
- And paternity leave?
- what about paternity policy?
- Is there a pat leave policy?
- May i know about pat leave?
- Can i know about paternity policy?
- Is there a pat leave policy?
- What is paternity leave policy?
- What is pat leave policy?
- What is paternity policy?

## intent: paternity_counted
- Will my paternity leave result in deduction of leave balance?
- will paternity leave be counted as regular leave?
- Is paternity counted as leave?
- will paternity be counted as leave?
- Am i going to loose my leaves due to paternity?

## intent: paternity_benefit
- Can i get paternity leave?
- Am i eligible for paternity leave?
- Who is eligible for paternity leave benefit?
- How [long](maternity_benefit: duration) can be the paternity leave?
- What is the [length](maternity_benefit: duration) of pat leave?
- What is the [duration](maternity_benefit:duration) of paternity leave?
- What is the [longest](maternity_benefit: duration) paternity leave i can take
- What is the [maximum length](maternity_benefit:duration) of paternity leave?
- How [many days](maternity_benefit:duration) of paternity
- Can i [extend](maternity_benefit:duration) my paternity leave?
- Can paternity leave be [extended](maternity_benefit:duration)?
- what is the [period](maternity_benefit: duration) of paternity leave?
- what is the [total length](maternity_benefit:duration) of paternity leave?
- will i get paternity leave for child [adoption](maternity_benefit:adoption)
- will i get paternity leave for [adopting](maternity_benefit:adoption) a child?
- Is paternity leave allwoed in case of [adoption](maternity_benefit:adoption)
- Can i get paternity leave if i [adopt](maternity_benefit:adoption)
- For how [many kids](maternity_benefit:child_number) can i take paternity leave?
- For how [many kids](maternity_benefit:child_number) is paternity policy applicable?
- For how [many children](maternity_benefit:child_number) can i get paternity leave?
- For how [many deliveries](maternity_benefit:child_number)
- Is paternity leave applicable only for [first child](maternity_benefit:child_number)?
- Is paternity leave applicable only for [second child](maternity_benefit:child_number)?
- This is my [third child](maternity_benefit:child_number). Will i get leave?
- For how [many childbirths](maternity_benefit:child_number) is paternity leave applicable?
- Will i get a [longer](maternity_benefit: duration) paternity leave for my [first delivery](maternity_benefit:child_number)?
- will i get a leave for my [second child](maternity_benefit:child_number)
- will i get a leave for my [first child](maternity_benefit:child_number)
- Will i get leave for any [number of childbirths](maternity_benefit:child_number)
- Is paternity bennefit applicable to a limited [number of children](maternity_benefit:child_number)
- This is my [second kid](maternity_benefit:child_number). Will i get paternity leave? 
- can i take my maternity leave in [multiple chunks](maternity_benefit:leave_split)
- How much of my paternity leave can i take before childbirth?
- can i [split](maternity_benefit:leave_split) my paternity leave?
- can i take pate leave in [multiple tranches](maternity_benefit:leave_split)
- can i [club](leave_benefit:club) my pat leave with other leaves?
- can i [combine](leave_benefit:club) my pat leave with other leaves?
- In how [many blocks](maternity_benefit:leave_split) can i avail paternity leave?
- Can i take paternity leave in [multiple blocks](maternity_benefit:leave_split)

<!--  --------------------------------------------------------------------------Synonnyms------------------------------------------------------------  -->
## synonym:child_number
- second child
- third child
- 3rd child
- 2nd child
- first child
- 1st child
- first dilivery
- second dilivery
- third dilivery
- 1st dilivery
- 2nd dilivery
- 3rd dilivery
- many deliveries
- many delivery
- many childs
- many children
- many kids
- many childbirths
- first pregnancy
- many pregnancies