*** Settings ***
Library    RequestsLibrary
Library    BuiltIn
Resource    ../tests/common_resources.robot
Resource    ../tests/common_keywords.robot

*** Variables ***
${VALID_INPUT_PAYLOAD}    {"number": 5}
${INVALID_INPUT_PAYLOAD}    {"number": -1}

*** Test Cases ***
Generate Fibonacci for valid input
    [Documentation]    Verify that the Fibonacci sequence is generated correctly for valid input.
    [Tags]    TC_FIBONACCI_001    High    Positive
    ${response}=    Post Request    uri=${BASE_URL}/fibonacci    json=${VALID_INPUT_PAYLOAD}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${response_body}=    Get Response Body    response=${response}
    Should Contain    ${response_body}    [0, 1, 1, 2, 3, 5]

Generate Fibonacci for invalid input
    [Documentation]    Ensure that the Fibonacci generation fails for invalid input.
    [Tags]    TC_FIBONACCI_002    High    Negative
    ${response}=    Post Request    uri=${BASE_URL}/fibonacci    json=${INVALID_INPUT_PAYLOAD}
    Should Be Equal As Numbers    ${response.status_code}    400
    ${response_body}=    Get Response Body    response=${response}
    Should Contain    ${response_body}    "error"  

*** Keywords ***
Stub Keyword
    [Arguments]    ${keyword_name}    @{args}
    Log    Stub: Called ${keyword_name} with arguments ${args}
    RETURN    ${EMPTY}