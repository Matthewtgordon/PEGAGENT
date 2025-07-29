# Website Ops Module

This module handles store operations via Shopify/Etsy connectors. All actions
are stubbed so no real payments occur.

## Setup

1. Copy `.env.template` to `.env` and fill in any keys if you plan to connect to
   real APIs (not required for dry run).
2. Load the variables:
   ```bash
   set -a && source ops_bridge/.env.template && set +a
   ```
   (Replace with your `.env` when ready.)

## Running Tasks

You can run tasks using `run_task` in a Python one-liner. For example:
```bash
python -c "from ops_bridge.ops_task_runner import run_task; import json; print(run_task(json.load(open('sample_tasks/status_shopify.json'))))"
```

## Sample Runs

### Refund
```
$ python -c "import json,ops_bridge.ops_task_runner as r;print(r.run_task(json.load(open('sample_tasks/refund_shopify.json'))))"
[NOTICE] APPROVAL REQUIRED: Refund 10.0 on shopify order 12345
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  ...
RuntimeError: Awaiting human approval
```

### Address Change
```
$ python -c "import json,ops_bridge.ops_task_runner as r;print(r.run_task(json.load(open('sample_tasks/address_change_shopify.json'))))"
[NOTICE] APPROVAL REQUIRED: Update address on shopify order 12345
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  ...
RuntimeError: Awaiting human approval
```

### Purchase (auto after delay)
```
$ python -c "import json,ops_bridge.ops_task_runner as r;print(r.run_task(json.load(open('sample_tasks/purchase_shopify.json'))))"
[NOTICE] PENDING: Create order on shopify
Auto-approve in 0.1 minutes unless you reply STOP.
{'ok': True, 'order_id': 'TBD', 'payload': {'sku': 'SKU-1', 'qty': 1, 'address': {'line1': '123 A St', 'city': 'X', 'region': 'CA'}}}
```
