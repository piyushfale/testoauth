from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id='80d4fbf6-4eaf-438e-9600-567b4441a2ca',
    tenant_id='0ab20ff7-b526-4a85-94b6-a7e83f5c0b9d',
    scopes={'api://80d4fbf6-4eaf-438e-9600-567b4441a2ca/access_as_user':'access_as_user'},
    allow_guest_users=True
    
)