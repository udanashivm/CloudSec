# 📘 AWS Lambda Function – List All S3 Buckets  

This repository contains an AWS Lambda function that retrieves all the S3 buckets in an AWS account and returns the list in JSON format.  
It is useful for inventory, compliance checks, or auditing AWS accounts.  

---

## 🚀 Features
- Lists all **S3 buckets** in the AWS account.  
- Returns both **bucket names** and **total count**.  
- Includes **error handling** and **logging to CloudWatch**.  
- Works with minimal **IAM permissions**.  

---

## 🛠 Prerequisites
Before deploying this function, ensure you have:  
- An **AWS account** with Lambda and S3 access.  
- **IAM Role** for Lambda with the following permission:  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    }
  ]
}
```

✅ Alternatively, you can attach the **AmazonS3ReadOnlyAccess** managed policy.  

---

## 📄 Lambda Function Code

File: `lambda_function.py`

```python
import json
import boto3

def lambda_handler(event, context):
    """
    AWS Lambda function to list all S3 buckets in the account.

    Parameters:
        event (dict): Event payload (not used here).
        context (object): Runtime information.

    Returns:
        dict: HTTP status code and JSON body containing bucket list and count.
    """
    # Create S3 client
    s3 = boto3.client("s3")

    try:
        # Fetch the list of buckets
        response = s3.list_buckets()

        # Extract bucket names
        buckets = [bucket['Name'] for bucket in response['Buckets']]

        # Log for CloudWatch
        print(f"Found {len(buckets)} buckets: {buckets}")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'bucket_count': len(buckets),
                'buckets': buckets
            })
        }

    except Exception as e:
        print(f"Error listing buckets: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

---

## ⚙️ Deployment Steps  

1. **Create a Lambda function** in AWS Console:  
   - Runtime: **Python 3.x**  
   - Permissions: Attach the IAM role with `s3:ListAllMyBuckets`.  

2. **Paste the code** into the Lambda editor (or upload via `.zip`/GitHub).  

3. **Deploy** the Lambda function.  

4. **Test** the function:  
   - Event: `{}` (empty JSON)  
   - Example Output:  

   ```json
   {
     "statusCode": 200,
     "body": "{\"bucket_count\": 3, \"buckets\": [\"my-bucket-1\", \"logs-bucket\", \"backup-bucket\"]}"
   }
   ```

---

## 📊 Example CloudWatch Logs  

```
Found 3 buckets: ['my-bucket-1', 'logs-bucket', 'backup-bucket']
```

---

## 🔒 Security Best Practices
- Use **least privilege IAM role** (only `s3:ListAllMyBuckets`).  
- Rotate IAM roles/keys regularly.  
- Enable **CloudTrail logging** to track access.  
- Restrict Lambda execution to trusted VPC/subnets if needed.  

---

## 📂 Repository Structure  

```
aws-s3-bucket-lister/
│── README.md              # Documentation
│── lambda_function.py     # Lambda code
│── policies/              
│    └── s3-list-policy.json  # Custom IAM policy (optional)
```

---

## 📌 Next Steps
- Extend the function to list **objects inside each bucket**.  
- Integrate with **AWS CloudWatch Events / EventBridge** to schedule regular checks.  
- Store results in **DynamoDB** or **S3** for auditing.  

---
