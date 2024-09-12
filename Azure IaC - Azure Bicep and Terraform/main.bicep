param location string = resourceGroup().location
param storageAccountName string = 'bicepwestus${uniqueString(resourceGroup().id)}'

resource newStorageAccountDabs 'Microsoft.Storage/storageAccounts@2023-04-01' = {
  name: storageAccountName
  location: 'westus'
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
  }
}
