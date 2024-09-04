# `usageplan.py` Documentation

## Purpose
The `usageplan.py` module manages usage plans for the tokens in the TokenSystem project. It provides functionalities to create, update, and retrieve usage plans for different token types.

## Key Functions/Classes

### `create_plan(plan_name, max_usage)`
- **Description**: Creates a new usage plan with the specified name and maximum usage limit.
- **Parameters**:
  - `plan_name`: Name of the usage plan.
  - `max_usage`: Maximum number of times the token can be used under this plan.
- **Returns**: None

### `update_plan(plan_id, new_max_usage)`
- **Description**: Updates the maximum usage limit for an existing usage plan.
- **Parameters**:
  - `plan_id`: ID of the plan to be updated.
  - `new_max_usage`: New maximum usage limit to be set.
- **Returns**: None

### `get_plan_details(plan_id)`
- **Description**: Retrieves details of a specific usage plan based on the plan ID.
- **Parameters**:
  - `plan_id`: ID of the plan to retrieve details for.
- **Returns**: Dictionary containing the details of the usage plan.

The `usageplan.py` module plays a crucial role in defining and managing usage plans for tokens within the TokenSystem project.