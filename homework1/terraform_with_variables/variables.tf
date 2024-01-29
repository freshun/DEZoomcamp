variable "credentials" {
  description = "My Credentials"
  default     = "../../../../../terraform-demo-key/elemental-leaf-411220-c43459f4ca11.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "elemental-leaf-411220"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "us-east1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "Homework Dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "elemental-leaf-411223-terraform-buckets"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}