## chitchat
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisiona OR ask_isbot OR ask_howold OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat

## deny ask_whatspossible
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp

## more chitchat
* greet
    - utter_greet
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisiona OR ask_isbot OR ask_howold OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisiona OR ask_isbot OR ask_howold OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat

## ask_whatspossible
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat

## ask_whatspossible more
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat