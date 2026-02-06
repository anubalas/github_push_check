*** Variables ***
${BASE_URL}    http://localhost:5000

*** Keywords ***
Stub Keyword
    [Arguments]    ${keyword_name}    @{args}
    Log    Stub: Called ${keyword_name} with arguments ${args}
    RETURN    ${EMPTY}