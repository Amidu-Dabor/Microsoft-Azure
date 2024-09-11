from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku, Kind

# Authenticate
credential = DefaultAzureCredential()
subscription_id = "bfb6a9d9-68c7-4b38-ab4e-0b8066f72a58"

# Create a resource management client
resource_client = ResourceManagementClient(credential, subscription_id)

# Resource group parameters
resource_group_name = "python-rg"
location = "eastus"

# Create the resource group
resource_client.resource_groups.create_or_update(resource_group_name, {"location": location})
print(f"Resource group '{resource_group_name}' created.")

# Create a storage management client
storage_client = StorageManagementClient(credential, subscription_id)

# Storage account parameters
count = 1
for _ in range(0, 3):
    storage_account_name = f"232pythonstorage{count}"  # Must be globally unique
    storage_params = StorageAccountCreateParameters(
        sku=Sku(name="Standard_LRS"),
        kind=Kind.BLOB_STORAGE,
        location=location,
        access_tier="Hot"  # Optional: Specify "Hot" or "Cool" for blob storage accounts
    )

    # Create the storage account
    storage_async_operation = storage_client.storage_accounts.begin_create(
        resource_group_name,
        storage_account_name,
        storage_params
    )
    count += 1

storage_account = storage_async_operation.result()
print(f"Storage account '{storage_account_name}' created in resource group '{resource_group_name}'.")

# Verify the account creation
# List all storage accounts in the resource group
storage_accounts = storage_client.storage_accounts.list_by_resource_group(resource_group_name)

for account in storage_accounts:
    print(f"Storage Account Name: {account.name}")
