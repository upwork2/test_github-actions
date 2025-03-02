
# Theory
- github action instances currently provides 4-vCPU with 16GB RAM for free plan
- github action consist of followng components
  - event triggers (`on:`)
    - defines the events that will trigger the workflow to run
    - `push`, `pull_request`, `workflow_dispatch`, `schedule` 
  - jobs (`jobs:`)
    - defines the actual tasks and actions to be executed when the workflow is triggered
    - each job is a set of steps than run on a specified runner (e.g. Ubuntu, Windows, etc.)
    - jobs can run in parallel or sequentially

# Examples

### action 1
- action is defined in `.github/workflows/script1.yml`, task of which is to execute `script1.py` file in the same directory
- user can manually execute action through following process
  - open this repository on github
  - set .env variable `API_TOKEN_1` at `settings -> security -> secrets and variables -> actions`
  - click on 'Actions' tab, click on 'select workflow'
  - select 'Execute Script#1' which is the name of workflow define under `name` variable in `script1.yml` file
  - click 'Run Workflow', in few seconds you will script execution details 

## action-2: S3 Parquet File Handling

This project includes a Python script `s3_parquet_handler.py` for interacting with Parquet files in AWS S3.

### Features
- Read Parquet files from S3
- Write Parquet files to S3
- List Parquet files in a bucket

### Prerequisites
- AWS S3 bucket access
- AWS credentials (set as GitHub secrets)
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

### Usage
Modify `s3_parquet_handler.py` to specify your S3 bucket and customize file operations.
