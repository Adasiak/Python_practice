tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/ap_sw_update/test_callables.py:

Fix boards configs:
  ✓ It creates all files

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/ap_sw_update/test_dag.py:

Create ap sw update:
  ✓ It returns dag
  ✓ It has proper tasks

tests/tests_ute_ca_manager/apps/test_execution_manager.py:

ExecutionManager:

  Create execution:
    ✓ It raises exception if passed exec id already exists
    ✓ It creates execution

  Monitor execution:
    ✓ It terminates workers if delta bigger than
    ✓ It calls update execution state
    ✓ It logs monitoring tasks exceptions
    ✓ It errors execution if workers does not register before timeout

  Start execution:
    ✓ It starts execution
    ✓ It unregisters execution if error occurs
    ✓ It returns if execution is already finished

  Terminate execution:
    ✓ It terminates execution

  Unregister execution:
    ✓ It unregisters execution

tests/tests_ute_ca_manager/backend/test_provision.py:

Execution:

  Choose builds:
    ✓ It sets all builds
    ✓ It throws error when classical build passed to cloud
    ✓ It throws error when cloud build passed to classical

  Create local execution dir:
    ✓ It creates local directory structure

  Create uca result file:
    ✓ It does nothing if file creation criteria are not met[attributes names0-attributes values0]
    ✓ It does nothing if file creation criteria are not met[attributes names1-attributes values1]
    ✓ It dumps data if file creation criteria are met[attributes names0-attributes values0]
    ✓ It dumps data if file creation criteria are met[attributes names1-attributes values1]

  Ensure execution is not cancelled:
    ✓ It returns false if execution is not errored
    ✓ It returns true if state is errored

  Get failed tasks:
    ✓ It gets list of failed tasks

  Get logs url:
    ✓ It gets logs url from file

  Get testline config:
    ✓ It calls all necessary actions
    ✓ It raises exception when config not found

  Get topology config:
    ✓ It calls all necessary actions
    ✓ It raises exception when config not found

  Send report:
    ✓ It sends report successfully without failed tasks
    ✓ It sends report successfully with failed tasks

  Start execution:
    ✓ It sets execution to errored and sends debug information
    ✓ It calls all necessary actions

  Terminate execution:
    ✓ It returns terminated if terminated properly
    ✓ It returns errored if termination failed

  Update execution state:
    ✓ It sets execution state to passed if all workers passed
    ✓ It sets execution state to errored if all workers finished and one of them errored
    ✓ It sets execution state to terminated if all workers finished and one of them terminated
    ✓ It sets execution state to failed if all workers finished and one of them failed
    ✓ It prioritizes errored state over all others
    ✓ It prioritizes terminated state over failed
    ✓ It does not update state if all workers still not finished

  Upload configuration:
    ✓ It uploads configs

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/bts_sw_update/test_callables.py:

Is targetbd available:
  ✓ It returns tasks to use targetbd from cache
  ✓ It adds targetbd path to xcom
  ✓ It returns tasks to use install files from cache
  ✓ It adds install files path to xcom
  ✓ It returns tasks to download install files for SBTS
  ✓ It returns tasks to do not download install files for pDU

Unpack targetbd:
  ✓ It unpacks targetbd from install files package

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/bts_sw_update/test_dag.py:

Create bts sw update:
  ✓ It returns dag
  ✓ It has proper tasks

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/classical_sw_update/test_callables.py:

Fill the interface template:
  ✓ It opens proper files calls jinja and creates correct content

Get device interface:
  ✓ It returns proper interface if matching device has been found
  ✓ It raises exception if no interface for device is found

Get names of netboot packages:
  ✓ It returns proper names of netboot packages

Is iphy available:
  ✓ It returns true if any device is sim device of sim type iphy
  ✓ It returns false if no device is sim device of sim type iphy

Is it simulator module:
  ✓ It returns true if device is simulator module
  ✓ It returns false if device is not simulator module

Is state sw uploaded:
  ✓ It returns true if sw uploaded is required state
  ✓ It returns false if configured is required state

Select check and mount method:
  ✓ It should return check sda1 and sda2 task
  ✓ It should return check sda2 and sda4 task
  ✓ It should return check mmcblk0p1 and mmcblk0p2 task

Select set netboot flags:
  ✓ It should return set netboot flags option1
  ✓ It should return set netboot flags option2
  ✓ It should return set netboot flags option3

Select sw update method:
  ✓ It should return perform bts sw update task
  ✓ It should return perform ap sw update task
  ✓ It should return perform cus sw update task for first device
  ✓ It should return empty list if cus is not first device
  ✓ It should return perform iphy sw update task

Sleep wrapper:
  ✓ It should sleep five seconds

Was iphy updated:
  ✓ It returns false when no result from task
  ✓ It returns false when iphy was not updated
  ✓ It returns true when iphy was updated

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/classical_sw_update/test_commands.py:

Create interface file:
  ✓ It builds proper command[xcom pull result0]

Install netboot packages:
  ✓ It builds proper command[xcom pull result0]

Set netboot flags option1 command:
  ✓ It builds proper command

Set netboot flags option2 command:
  ✓ It builds proper command

Set netboot flags option3 command:
  ✓ It builds proper command

Start netboot service for device:
  ✓ It builds proper command[xcom pull result0]

Stop netboot service for device:
  ✓ It builds proper command[xcom pull result0]

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/classical_sw_update/test_dag.py:

Create check fs and mount partitions:
  ✓ It returns dag
  ✓ It has proper tree

Create configure netboot:
  ✓ It returns dag
  ✓ It has proper tree

Create perform classical sw update:
  ✓ It returns dag
  ✓ It has proper tree

Create reboot and perform sw udpate dag:
  ✓ It returns dag
  ✓ It has proper tree

Create reboot dag:
  ✓ It returns dag
  ✓ It has proper tree

Create reboot device from netboot:
  ✓ It returns dag
  ✓ It has proper tree

Create reboot device to netboot:
  ✓ It returns dag
  ✓ It has proper tree

Create reboot sm and iphy subdag:
  ✓ It returns dag
  ✓ It has proper tree

Create set netboot flags dag:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/clean_up_partition/test_commands.py:

Change config directory permissions command:
  ✓ It generates correct command

Crasign swconfig command:
  ✓ It generates correct command

Craverify swconfig command:
  ✓ It generates correct command

Create swconfig command:
  ✓ It generates correct command

Ensure directory exists command:
  ✓ It generates correct command

Remove directory content on partition command:
  ✓ It generates correct command

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/clean_up_partition/test_dag.py:

Create clean up partition:
  ✓ It returns dag
  ✓ It has proper tasks

tests/tests_ute_ca/cli/test_apiserver.py:

Typer app:
  ✓ It has the serve command

  Serve callback:
    ✓ It reads the apiserver configuration section
    ✓ It launches systemd notifier only when the notify option is set[True]
    ✓ It launches systemd notifier only when the notify option is set[False]
    ✓ It sets the proper readiness probe for the notifier
    ✓ It launches uvicorn under configured host and port
    ✓ It ignores uvicorn reload option when systemd notify is set[True-True]
    ✓ It ignores uvicorn reload option when systemd notify is set[False-True]

  Serve command:
    ✓ It takes user options[parameters0]
    ✓ It takes user options[parameters1]
    ✓ It takes user options[parameters2]
    ✓ It takes user options[parameters3]
    ✓ It takes user options[parameters4]
    ✓ It takes user options[parameters5]
    ✓ It returns non zero exit code for undefined parameters

tests/tests_ute_ca/cli/test_main.py:
  ✓ It has the watch command

  Watch callback:
    ✓ It starts the systemd notifier with proper readiness probes

tests/tests_ute_ca/cli/test_manager.py:
  ✓ It has the serve command

  Serve callback:
    ✓ It reads the manager configuration section
    ✓ It launches systemd notifier only when the notify option is set[True]
    ✓ It launches systemd notifier only when the notify option is set[False]
    ✓ It sets the proper readiness probe for the notifier
    ✓ It launches uvicorn under configured host and port
    ✓ It ignores uvicorn reload option when systemd notify is set[True-True]
    ✓ It ignores uvicorn reload option when systemd notify is set[False-True]

  Serve command:
    ✓ It takes user options[parameters0]
    ✓ It takes user options[parameters1]
    ✓ It takes user options[parameters2]
    ✓ It takes user options[parameters3]
    ✓ It takes user options[parameters4]
    ✓ It takes user options[parameters5]
    ✓ It returns non zero exit code for undefined parameters

tests/tests_ute_ca_manager/utils/clients/test_context.py:

AgentContextApiClient:

  Create context:
    ✓ It returns correct response json
    ✓ It raises APIServerResponseError in case of error

tests/tests_ute_ca_manager/utils/clients/test_core.py:

AsyncHttpClient:
  ✓ It raises an error when config path does not exist
  ✓ It raises an error when config section does not exist

  Get:
    ✓ It calls get properly
    ✓ It raises apiresponse exception on http error

  Post:
    ✓ It calls post properly
    ✓ It raises apiresponse exception on http error

  Put:
    ✓ It calls put properly
    ✓ It raises apiresponse exception on http error

  Server address:
    ✓ It returns the server address

  Stream:
    ✓ It raises apiresponse exception on http error

tests/tests_ute_ca_manager/utils/clients/test_execution.py:

ExecutionApiClient:
  ✓ Get calls api properly
  ✓ Get raises exception when status code different than 200
  ✓ Get all calls api properly
  ✓ Get all raises exception when status code different than 200
  ✓ Update execution state calls api properly
  ✓ Update execution state raises exception when status code different than 200
  ✓ Save execution debug calls api properly
  ✓ Save execution debug raises exception when status code different than 200

tests/tests_ute_ca_manager/utils/clients/test_file.py:

FileApiClient:

  Download file:
    ✓ It downloads files

  Upload file:
    ✓ It uploads files
    ✓ It raises response error if not status code eq 200

tests/tests_ute_ca_manager/utils/clients/test_task.py:

TaskApiClient:

  Get all tasks info:
    ✓ It gets all failed tasks information

tests/tests_ute_ca_manager/utils/clients/test_worker.py:

WorkerApiClient:
  ✓ Get all workers info calls api properly
  ✓ Update worker state calls api properly
  ✓ Update raises exception when status code different than 200

WorkerShellClient:
  ✓ Start workers creates asyncio tasks with correct method and params
  ✓ Start worker calls shell client properly
  ✓ Terminate workers creates asyncio tasks with correct method and params
  ✓ Terminate worker kills worker
  ✓ Kill worker over ssh executes kill command and returns status
  ✓ Kill worker over ssh retries after first timeout
  ✓ Kill worker over ssh returns error after second timeout
  ✓ Kill worker over ssh returns error if ssh execution error
  ✓ Start aria2c service on all nodes creates asyncio tasks with correct method and params
  ✓ Stop aria2c service on all nodes creates asyncio tasks with correct method and params
  ✓ Start aria2c service on node executes proper ssh command
  ✓ Start aria2c service on node reacts to ssh execution error
  ✓ Start aria2c service on node reacts to ssh execution timeout
  ✓ Stop aria2c service on node executes proper ssh command
  ✓ Stop aria2c service on node reacts to ssh execution error
  ✓ Stop aria2c service on node reacts to ssh execution timeout
  ✓ Create execution dir on remote node calls the appropriate command
  ✓ Sync execution dir on remote node calls the appropriate command
  ✓ Create and sync execution dir on remote nodes
  ✓ Sync log dir from remote calls the appropriate command
  ✓ Sync log dir to remote calls the appropriate command
  ✓ Sync log dir on all nodes
  ✓ Sync logs does not execute because there is only 1 node
  ✓ Sync logs does not execute because testline config has not been parsed yet

tests/tests_ute_ca_agentctl/commands/test_base.py:

APICallCommand:
  ✓ It inherits from Command
  ✓ It has the api addr attr

  Handle http error:
    ✓ It logs http errors

Command:
  ✓ It defines an abstract
  ✓ It enforces the execute method

Get api addr:
  ✓ It returns the api addr
  ✓ It raises an error if apiserver section is missing

tests/tests_ute_ca_agentctl/commands/test_provision.py:

CancelCommand:

  Backend:
    ✓ It cancels provisioning

  Cli:
    ✓ It calls the appropriate backend
    ✓ It requires execution id

InfoCommand:

  Backend:
    ✓ It sends info request

  Cli:
    ✓ It calls the appropriate backend
    ✓ It requires execution id

RunCommand:

  Backend:
    ✓ It sends provisioning request
    ✓ It downloads debug if needed
    ✓ It uploads configuration if provided
    ✓ It sends reservation id if env var is set
    ✓ It zips and sends the config file
    ✓ It raises an error when the config file is not a dir or file[is not dir]
    ✓ It raises an error when the config file is not a dir or file[is not file]
    ✓ It gets execution info
    ✓ It saves env variables
    ✓ It checks if the execution is ongoing[scenario0]
    ✓ It checks if the execution is ongoing[scenario1]
    ✓ It checks if the execution is ongoing[scenario2]
    ✓ It retrieves builds and resolved label found by manager
    ✓ It doesnt update builds if execution fails

  Cli:
    ✓ It calls the appropriate backend
    ✓ It requires a build name
    ✓ It requires a label

Terminate hanging execution:
  ✓ It terminates if execution id and ongoing
  ✓ It does not terminate if no execution id
  ✓ It does not terminate if execution id and not ongoing

tests/tests_ute_ca_agentctl/commands/test_signals.py:

Cancel execution handler:
  ✓ It raises error if provision response is not available
  ✓ It raises error if provision response has error
  ✓ It raises error if cancel action has 425 status code
  ✓ It returns if cancel action finished with error code 423
  ✓ It returns if cancel action finished with error code 500
  ✓ It returns if cancel action failed and response has no json
  ✓ It returns if cancel action finished with error different than 425 or 423
  ✓ It calls function to stop agentctl if cancel action finished properly and exits

Configure signals:
  ✓ It configures all needed signals

tests/tests_ute_ca_worker/unittests/dag/commissioned/commissioned/test_callables.py:

Download targetbd from vdu:
  ✓ It downloads targetbd

Is commission hook present:
  ✓ It returns true when hook present
  ✓ It returns false when hook not present

Is commissioned final state:
  ✓ It returns true when commissioned final state
  ✓ It returns false when commissioned not final state

Is ocp controller available:
  ✓ It returns true when ocp controller is available
  ✓ It returns false when ocp controller is not available

Is open stack controller available:
  ✓ It returns true when controller is available
  ✓ It returns false when controller is not available

Select devices to power off:
  ✓ It returns powerr off sm when sm is available
  ✓ It returns powerr off sim when sim is available
  ✓ It returns two tasks when both sm and sim are available
  ✓ It returns two tasks when two sim are available

Select type of commissioning:
  ✓ It returns sm commissioning
  ✓ It returns sim configuration
  ✓ It returns vcu commissioning
  ✓ It returns cus configuration for each cus simulator module
  ✓ It returns sim configuration for each simulator module

tests/tests_ute_ca_worker/unittests/dag/commissioned/commissioned/test_dag.py:

Create commissioned:
  ✓ It returns dag
  ✓ It has proper tree
  ✓ It has perform vcu commissioning for vran2

tests/tests_ute_ca_worker/unittests/dag/configured/configured/test_callables.py:

Check if fullrack and master node:
  ✓ It returns true if fullrack and master node[config0-True]
  ✓ It returns true if fullrack and master node[config1-False]
  ✓ It returns true if fullrack and master node[config2-False]

Check if fullrack and slave node:
  ✓ It returns true if fullrack and slave node[config0-False]
  ✓ It returns true if fullrack and slave node[config1-True]
  ✓ It returns true if fullrack and slave node[config2-False]

Count retries:
  ✓ It pushes new timestamp

Select devices to reboot:
  ✓ It returns reboot sm when sm is available
  ✓ It returns reboot sim when sim is available
  ✓ It returns two tasks when both sm and sim are available
  ✓ It returns two tasks when two sim are available
  ✓ It returns reboot not needed if no sm and no sim is avaiable

Send synchronization information:
  ✓ It sends configured reached synchronization information
  ✓ It sends reboot performed synchronization information

Wait for synchronization information:
  ✓ It waits for configured reached synchronization information
  ✓ It waits for reboot performed synchronization information

tests/tests_ute_ca_worker/unittests/dag/configured/configured/test_dag.py:

Create configured:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/core/test_args.py:

PullAvailable:
  ✓ It resolves xcoms to args
  ✓ It raises when args count doesnt match
  ✓ It does not raise without expected count

tests/tests_ute_ca_worker/unittests/core/test_command.py:

BaseCommand:
  ✓ It generates simple command
  ✓ It generates complex command
  ✓ It generates command with flag list
  ✓ It generates command with switch list

CommandChain:
  ✓ It concatenates commands

ParametrizedCommand:
  ✓ It pulls correct value from xcom
  ✓ It pulls correct value from variable

tests/tests_ute_ca_worker/unittests/core/test_config.py:

LazyWorkerContext:

  Builds:
    ✓ It raise exception if setup was not called

  Devices:
    ✓ It raise exception if setup was not called

  Get device:
    ✓ It raise exception if setup was not called

  Get devices:
    ✓ It raise exception if setup was not called

  Label:
    ✓ It raise exception if setup was not called

  Node id:
    ✓ It raise exception if setup was not called

  Raw:
    ✓ It raise exception if setup was not called

  Required state:
    ✓ It raise exception if setup was not called

  Variant:
    ✓ It raise exception if setup was not called

Prepare builds for node:
  ✓ It should return prepared builds
  ✓ It should return prepared builds for second node with bts build from first node

tests/tests_ute_ca_worker/unittests/core/test_dag.py:

Dag:
  ✓ It can be created
  ✓ It is a context manager
  ✓ It supports nested dags
  ✓ It has custom representation
  ✓ It allows to set edge
  ✓ It allows to add node
  ✓ It raises error if two dags with same name will be created
  ✓ It raises error if edge will be create to background task
  ✓ It raises error if task has edge to two branch tasks
  ✓ It raises error if second task with same name was added
  ✓ It returns dag as dict of dicts
  ✓ It returns reactflow representation

tests/tests_ute_ca_worker/unittests/core/test_executor.py:

DagExecutor:

  Execute:
    ✓ It ends when endevent was routed
    ✓ It sends heartbeat when heartbeatevent was routed
    ✓ It ends when dagcompletionevent was routed with proper id
    ✓ It raises error if dagcompletionevent was routed with failed status
    ✓ It routes tasktoexecuteevent when tasktoschedule was routed
    ✓ It routes taskscheduledevent when tasktoschedule was routed
    ✓ It routes taskpassedevent when taskexecutedevent was routed and is positive
    ✓ It routes taskfailedevent when taskexecutedevent was routed and is negative
    ✓ It raises error when internalerrorevent was routed
    ✓ It omits dummy task
    ✓ It registers whole dag at the beginning of the dag execution

TaskExecutor:
  ✓ It executes passed task
  ✓ It executes failed task

tests/tests_ute_ca_worker/unittests/core/test_hearbeat.py:

HeartbeatTrigger:
  ✓ It generates heartbeatevent

tests/tests_ute_ca_worker/unittests/core/test_lazy_device.py:

LazyDevice:

  Filter services:
    ✓ It raises if device is not initialized
    ✓ It calls filter services method of inner device

  Get capacity units:
    ✓ It raises if device is not initialized
    ✓ It raises if device has no capacity units
    ✓ It returns capacity units if device has any

  Get connections:
    ✓ It raises if device is not initialized
    ✓ It raises if device is not vm
    ✓ It returns connections if device is vm

  Get pdu:
    ✓ It raises if device is not initialized
    ✓ It raises if device has no pdu
    ✓ It returns pdu if device has one

  Get service:
    ✓ It raises if device is not initialized
    ✓ It calls get service method of inner device

  Properties:
    ✓ It is truthy if device was provided
    ✓ It is falsy if device was not provided
    ✓ It returns proper uid
    ✓ It returns default hw id if device is not initialized
    ✓ It returns hw id of inner device
    ✓ It returns default hw name if device is not initialized
    ✓ It returns hw name of inner device
    ✓ It returns default hw type if device is not initialized
    ✓ It returns hw type of inner device
    ✓ It raises when device is not initialized and prop is requested
    ✓ It returns prop of inner device
    ✓ It returns correct string representation

tests/tests_ute_ca_worker/unittests/core/test_task.py:

BinaryChoiceTask:
  ✓ It returns passed tasks if callable returns true
  ✓ It returns failed tasks if callable returns false

BranchTask:
  ✓ It returns single task name
  ✓ It returns multiple task names
  ✓ It returns empty list
  ✓ It returns None

PythonTask:
  ✓ It returns result from callable
  ✓ It returns passed args and kwargs

ShellTask:
  ✓ It executes shell command

SshTask:
  ✓ It executes ssh command

SubDagTask:

  Execute:
    ✓ It returns subdag

  Subdag:
    ✓ It returns subdag

Task:
  ✓ It raises error when run is not overriden
  ✓ It raises ValueError when both max retries and timeout with retries is given
  ✓ It calls normally when run if overriden

  Args str:
    ✓ It returns args and kwargs string

  Context:
    ✓ It allows to set task context
    ✓ It raises error if context is set second time

  Dag:
    ✓ It returns dag parent

  Eq:
    ✓ It returns true if task id are the same

  Execute:
    ✓ It executes run method
    ✓ It executes run method with args and kwargs
    ✓ It raises error if context is not set
    ✓ It resolves xcom args if provided
    ✓ It resolves xcom kwargs if provided
    ✓ It resolves variable args if provided
    ✓ It resolves variable kwargs if provided

  Hash:
    ✓ It returns proper value

  Id:
    ✓ It allows to set task id
    ✓ It raises error if id is set second time

  Ignored exceptions:
    ✓ It raises exception when not ignored
    ✓ It does not raise exception when exception is ignored
    ✓ It raises exception when different exception is ignored

  Lshift:
    ✓ It creates edge with other task
    ✓ It creates edge with list of tasks
    ✓ It creates edge between list and single task
    ✓ It returns other task

  Name:
    ✓ It returns proper task name
    ✓ It returns proper task name for nested dags

  Repr:
    ✓ It returns task id

  Retries:
    ✓ It returns 0 by default
    ✓ It returns set retries value

  Retry delay:
    ✓ It returns default value
    ✓ It returns set retry delay value

  Rshift:
    ✓ It creates edge with other task
    ✓ It creates edge with list of tasks
    ✓ It creates edge between list and single task
    ✓ It returns other task

  Timeout:
    ✓ It returns default timeout
    ✓ It returns set timeout value

tests/tests_ute_ca_worker/unittests/core/test_testline.py:

Device:
  ✓ It can filter services[device0-expected0]
  ✓ It can filter services[device1-expected1]
  ✓ It can get service
  ✓ It raises exception when no service found
  ✓ It raises exception when more than one service found

tests/tests_ute_ca_worker/unittests/core/test_variable.py:

VariableClient:

  Pull:
    ✓ It routes variable pull event and wait for variable data event
    ✓ It reads proper variable data event
    ✓ It returns none if end event was routed
    ✓ It raises error if proper variable data does not appear

  Push:
    ✓ It routes variable push event

tests/tests_ute_ca_worker/unittests/core/test_ws.py:

ApiServerEventSender:
  » It connects to proper endpoint
  » It sends events via websocket[event0]
  » It sends events via websocket[event1]
  » It sends events via websocket[event2]

tests/tests_ute_ca_worker/unittests/core/test_xcom.py:

XComClient:

  Pull:
    ✓ It routes xcom pull event and wait for xcom data event
    ✓ It reads proper xcom data event
    ✓ It returns none if end event was routed
    ✓ It raises error if proper xcom data does not appear

  Push:
    ✓ It routes xcom push event

XComScopeValidator:
  ✓ It validates xcom scope
  ✓ It raises validation error

XCom class:
  ✓ It returns correct string representation
  ✓ It returns task name
  ✓ It returns xcom key

tests/tests_ute_ca_worker/unittests/dag/commissioned/create_stack/test_callables.py:

Callables:
  ✓ It extracts addons file to correct directory
  ✓ It copies custom env file to directory with extracted addons
  ✓ It updates env parameters

Create stack:
  ✓ It creates stack

tests/tests_ute_ca_worker/unittests/dag/commissioned/create_stack/test_dag.py:

Create stacks subdag:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_apiserver/crud/test_context_crud.py:

Create agent context:
  ✓ It creates agent context

Show agent context:
  ✓ It shows agent context
  ✓ It raises does not exist exception

tests/tests_ute_ca_apiserver/crud/test_execution_crud.py:

Check if pending state:
  ✓ It raise retry error for pending state
  ✓ It wont raise retry error for non pending state

Ensure no active executions:
  ✓ It raises exception if any execution is running

Get execution debug:
  ✓ It returns the execution debug

Monitor pending state:
  ✓ It fails execution with debug information if retry error is raised
  ✓ It does nothing if execution is running

Register execution:
  ✓ It registers new executions

Save execution debug:
  ✓ It stores the execution debug in db

Show execution info:
  ✓ It shows info about a single execution
  ✓ It raises does not exist exception

Show execution info all:
  ✓ It shows info about all executions[None-4]
  ✓ It shows info about all executions[scenario1-0]
  ✓ It shows info about all executions[scenario2-1]

Update execution state:
  ✓ It updates the execution state
  ✓ It raises does not exist exception

tests/tests_ute_ca_apiserver/crud/test_file_crud.py:

Download file:
  ✓ It downloads files from the database
  ✓ It raises checksum mismatch error
  ✓ It raises does not exist error

Upload file:
  ✓ It uploads files to the database
  ✓ It raises checksum mismatch error

tests/tests_ute_ca_apiserver/crud/test_provision_crud.py:

Cancel provisioning:
  ✓ It cancels provisioning
  ✓ It raises manager response error

Show all provisioning info:
  ✓ It shows information about all provisionings[None-4]
  ✓ It shows information about all provisionings[Running-1]

Show provisioning info:
  ✓ It shows information about a single provisioning
  ✓ It raises does not exist exception

Start provisioning:
  ✓ It sends provisioning request to manager
  ✓ It raises manager response error

tests/tests_ute_ca_apiserver/crud/test_task_crud.py:

Show all tasks info:
  ✓ It shows all tasks info

Show task info:
  ✓ It shows task info

Update task:
  ✓ It updates task entries[scenario0]
  ✓ It updates task entries[scenario1]

tests/tests_ute_ca_apiserver/crud/test_worker_crud.py:

All workers info:
  ✓ It shows information about all workers[scenario0-4]
  ✓ It shows information about all workers[scenario1-2]
  ✓ It shows information about all workers[scenario2-1]
  ✓ It shows information about all workers[scenario3-1]
  ✓ It shows information about all workers[scenario4-1]
  ✓ It shows information about all workers[scenario5-1]
  ✓ It shows information about all workers[scenario6-0]

Register worker:
  ✓ It registers new workers
  ✓ It raises does not exist exception

Show worker info:
  ✓ It shows information about a single worker
  ✓ It raises does not exist exception

Update worker:
  ✓ It updates worker entries[scenario0]
  ✓ It updates worker entries[scenario1]
  ✓ It updates worker entries[scenario2]
  ✓ It raises does not exist exception
  ✓ It raises nothing to update exception

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/cus_sw_update/test_callables.py:

Cus executor config remote reload:
  ✓ It properly reloads
  ✓ It throws error when no matching regex
  ✓ It throws error when incorrect return code

Download auto config repo:
  ✓ It downloads repo properly

Generate config files:
  ✓ It generates config files without variant
  ✓ It generates config files with variant

Update cus ini:
  ✓ It updates the file
  ✓ It raises error when path doesnt exist

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/cus_sw_update/test_commands.py:

Create ip address set command:
  ✓ It generates correct command

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/cus_sw_update/test_dag.py:

Create cus sw update:
  ✓ It returns dag
  ✓ It has proper tasks

tests/tests_ute_ca_worker/unittests/dag/test_main.py:

Create root:
  ✓ It returns dag[worker custom config0]
  ✓ It returns dag[worker custom config1]
  ✓ It returns dag[worker custom config2]
  ✓ It returns dag[worker custom config3]
  ✓ It returns dag[worker custom config4]
  ✓ It returns dag[worker custom config5]
  ✓ It returns dag[worker custom config6]
  ✓ It returns dag[worker custom config7]
  ✓ It returns dag[worker custom config8]
  ✓ It has proper tree

Is commissioning needed:
  ✓ It returns true when commissioned is required state
  ✓ It returns false when sw uploaded is required state

Is configured or on air needed:
  ✓ It returns correct task when sw uploaded is required state
  ✓ It returns correct task when configured is required state
  ✓ It returns correct task when on air is required state

Is ssh only required state:
  ✓ It returns true when ssh only is required state
  ✓ It returns false when commissioned is required state

tests/tests_ute_ca_apiserver/endpoints/test_context_api.py:

Create agent context:
  ✓ It creates agent context
  ✓ It validates agent context mode[context0-expected0]
  ✓ It validates agent context mode[context1-expected1]
  ✓ It validates agent context required state[context0-expected0]
  ✓ It validates agent context required state[context1-expected1]

Show agent context:
  ✓ It returns agent context
  ✓ It handles errors

tests/tests_ute_ca_apiserver/endpoints/test_execution_api.py:

Get execution debug:
  ✓ It retrieves the execution debug
  ✓ It returns 404 if debug does not exist

Register execution:
  ✓ It registers new executions
  ✓ It handles execution already running exception
  ✓ It validates execution type[scenario0-expected0]
  ✓ It validates execution type[scenario1-expected1]

Save execution debug:
  ✓ It saves the execution debug

Show all executions info:
  ✓ It shows information about all executions[scenario0-expected0]
  ✓ It shows information about all executions[scenario1-expected1]
  ✓ It shows information about all executions[scenario2-expected2]
  ✓ It validates the state filter

Show execution info:
  ✓ It shows info about a single execution
  ✓ It handles errors

Update execution state:
  ✓ It updates execution db entries[scenario0]
  ✓ It updates execution db entries[scenario1]
  ✓ It updates execution db entries[scenario2]
  ✓ It handles errors
  ✓ It validates execution state[scenario0-expected0]
  ✓ It validates execution state[scenario1-expected1]

tests/tests_ute_ca_apiserver/endpoints/test_file.py:

Download file:
  ✓ It downloads files from database
  ✓ It reacts to does not exist error
  ✓ It reacts to checksum mismatch error

Remove temporary file:
  ✓ It removes the provided path

Upload file:
  ✓ It uploads files to database
  ✓ It reacts to checksum mismatch

tests/tests_ute_ca_apiserver/endpoints/test_health_api.py:

Check health:
  ✓ It responds to get requests

tests/tests_ute_ca_apiserver/endpoints/test_provision_api.py:

Cancel provisioning:
  ✓ It cancels provisioning
  ✓ It handles manager response error other than 423 and 425
  ✓ It handles manager specific error responses[423]
  ✓ It handles manager specific error responses[425]

Show all provisioning info:
  ✓ It returns information about all executions[scenario0-expected0]
  ✓ It returns information about all executions[scenario1-expected1]
  ✓ It returns information about all executions[scenario2-expected2]

Show provisioning info:
  ✓ It shows info about a single provisioning
  ✓ It handles does not exist error

Start provisioning:
  ✓ It starts new provisioning
  ✓ It handles manager response error

tests/tests_ute_ca_apiserver/endpoints/test_worker_api.py:

Register worker:
  ✓ It registers new workers
  ✓ It handles errors

Show worker info:
  ✓ It shows info about a single worker
  ✓ It handles errors

Show worker info all:
  ✓ It shows info about all executions[scenario0-expected0]
  ✓ It shows info about all executions[scenario1-expected1]
  ✓ It shows info about all executions[scenario2-expected2]
  ✓ It shows info about all executions[scenario3-expected3]
  ✓ It shows info about all executions[scenario4-expected4]
  ✓ It validates the state filter

Update worker:
  ✓ It updates worker records[data0]
  ✓ It updates worker records[data1]
  ✓ It updates worker records[data2]
  ✓ It handles errors[scenario0-expected0]
  ✓ It handles errors[scenario1-expected1]

Worker ws in:
  ✓ It creates a websocket connection

Worker ws out:
  ✓ It creates a unique websocket connection

tests/tests_ute_ca_manager/endpoints/test_health_endpoints.py:

Check health:
  ✓ It responds to get requests

tests/tests_ute_ca_manager/endpoints/test_provision_endpoints.py:

Provision endpoints:

  Cancel provisioning:
    ✓ It terminates agent provisioning when execution is running
    ✓ It errors agent provisioning
    ✓ It shows error for api response error
    ✓ It does not terminate agent provisioning when execution is finished
    ✓ It shows specific error if execution is already in termination
    ✓ It shows specific error if execution is in pending state

  Create execution:
    ✓ It creates execution instance properly

  Run provisioning:
    ✓ It runs worker provisioning

tests/tests_ute_ca_worker/unittests/dag/shared/execute_hook/test_commands.py:

Execute hook command:
  ✓ It generates correct command
  ✓ It raises exeception when hook not found

Install hook command:
  ✓ It generates correct command
  ✓ It raises exeception when hook not found

tests/tests_ute_ca_worker/unittests/dag/shared/execute_hook/test_dag.py:

ExecuteHook:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_apiserver/apps/scheduler/handlers/test_dag.py:

Dag completion event handler:
  ✓ It checks if tasks are finished[scenario factory0]
  ✓ It checks for unfinished bg tasks[scenario factory0]
  ✓ It cancels unfinished bg tasks[scenario factory0]
  ✓ It resolves the dag state[scenario factory0-Passed]
  ✓ It resolves the dag state[scenario factory1-Failed]
  ✓ It notifies the worker queue[scenario factory0]
  ✓ It adds EndEvent to worker queue[scenario factory0]
  ✓ It handles subdags[scenario factory0]

Dag event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts
  ✓ It locks dag objects[scenario factory0]
  ✓ It raises an error if dag does not exist

Dag registration event handler:
  ✓ It registers new dags
  ✓ It triggers dag scheduled event
  ✓ It registers dag tasks
  ✓ It marks root tasks
  ✓ It updates task dependencies

Dag scheduled event handler:
  ✓ It marks dag as scheduled[scenario factory0]
  ✓ It triggers scheduling of root tasks[scenario factory0]

tests/tests_ute_ca_apiserver/apps/scheduler/handlers/test_handlers_core.py:

Conditional locked event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts

Event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts

Locked event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts

Simple event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts

tests/tests_ute_ca_apiserver/apps/scheduler/handlers/test_task.py:

Dummy task event handler:
  ✓ It creates a task execution instance[scenario factory0]
  ✓ It spawns task passed event[scenario factory0]

Task event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts
  ✓ It locks dag objects[scenario factory0]
  ✓ It raises an error if dag does not exist

Task failed event handler:
  ✓ It changes task state to failed[scenario factory0]
  ✓ It changes task state to retrying[scenario factory0]
  ✓ It changes task state to failed if retrying but special exception present[scenario factory0]
  ✓ It changes task state to failed if retrying but timeout with retries reached[scenario factory0]

Task passed event handler:
  ✓ It changes task state to passed[scenario factory0]

Task scheduled event handler:
  ✓ It creates a task execution instance[scenario factory0]
  ✓ It sets state to scheduled[scenario factory0]
  ✓ It sets first schedule time when it is first execution[scenario factory0]
  ✓ It does not set first schedule time when it is not first execution[scenario factory0]

Task to schedule event handler:
  ✓ It sets root tasks to schedule[scenario factory0]
  ✓ It checks obligatory predecessor states[scenario factory0]
  ✓ It checks task triggers[scenario factory0]
  ✓ It triggers skipping of tasks[scenario factory0]
  ✓ It spawns dummy task event for dummy task[scenario factory0]
  ✓ It triggers skipping nonmandatory task if any dag has failed[scenario factory0]

tests/tests_ute_ca_apiserver/apps/scheduler/handlers/test_variable.py:

Var pull event handler:
  ✓ It returns a stored variable
  ✓ It raises an error when variable is missing

Var push event handler:
  ✓ It creates new variable entries
  ✓ It raises an error on unique constraint violation

Variable event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts

tests/tests_ute_ca_apiserver/apps/scheduler/handlers/test_worker.py:

Worker errored event handler:
  ✓ It changes states for dags and tasks[scenario factory0]

tests/tests_ute_ca_apiserver/apps/scheduler/handlers/test_xcom.py:

Xcom event handler:
  ✓ It cannot be instantiated
  ✓ It contains abstracts
  ✓ It locks dag objects[scenario factory0]
  ✓ It raises an error if task execution does not exist[scenario factory0]

Xcom pull event handler:
  ✓ It pulls xcom entries for given task from return value[scenario factory0]
  ✓ It pulls xcom entries for given task[scenario factory0]
  ✓ It raises an error if task has no return value[scenario factory0]
  ✓ It raises an error if task has no xcom key[scenario factory0]

Xcom push event handler:
  ✓ It adds xcom entries[scenario factory0]
  ✓ It disallows key overlaps in xcom[scenario factory0]

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/iphy_sw_update/test_callables.py:

Install puttibatti:
  ✓ It creates new virtualenv
  ✓ It installs puttibatti dependencies

Parse checksum file:
  ✓ It parses properly checksum file

Run puttibatti:
  ✓ It runs puttibatti command[parsed config0-1-192.168.200.126-10.0.2.2 10.0.2
  ✓ It runs puttibatti command[parsed config1-2-192.168.200.127-10.0.2.4 10.0.2
  ✓ It runs puttibatti command[parsed config2-1-192.168.200.127-10.0.2.4 10.0.2

Switch partition:
  ✓ It switches partition to passive

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/iphy_sw_update/test_dag.py:

Create iphy sw update:
  ✓ It returns dag

tests/tests_ute_ca_worker/unittests/lib/test_adets.py:

Adets on device:
  ✓ It verifies adets
  ✓ It throws exception when statuses are incorrect
  ✓ It throws exception when cpu statuses are incorrect

Adets serializer:
  ✓ It serializes cpus
  ✓ It serializes units

tests/tests_ute_ca_worker/unittests/lib/test_admin.py:

Admin session:
  ✓ It setups new admin session
  ✓ It teardowns admin session

tests/tests_ute_ca_worker/unittests/lib/test_artifactory.py:

Prioritize servers:
  ✓ It returns list of available servers urls
  ✓ It returns empty list if no servers available

tests/tests_ute_ca_worker/unittests/lib/test_coam_admin.py:

Connect to coam cu:
  ✓ It setups new admin session
  ✓ It teardowns admin session
  ✓ It retries connection when error
  ✓ It reraises error after retry

Connect to coam vdu:
  ✓ It setups new admin session
  ✓ It teardowns admin session
  ✓ It reraises error after retry

tests/tests_ute_ca_worker/unittests/lib/test_openstack.py:

Get checksum:
  ✓ It gets checksum
  ✓ It should raise exception when image unable to find
  ✓ It gets checksum image not found

Get image sources:
  ✓ It gets image sources

Load image to controller:
  ✓ It loads image successfully

Openstack session:
  ✓ It creates openstack session

Verify image checksum:
  ✓ It verifies image checksum successfully
  ✓ It verifies image checksum unsuccessfully
  ✓ It verifies image checksum unsuccessfully after runtime error on main source

tests/tests_ute_ca_worker/unittests/lib/test_pdu.py:

Pdu session:
  ✓ It creates pdu session for pdu aten
  » It creates pdu session for pdu fpfh
  ✓ It creates pdu session for pdu gude
  ✓ It creates pdu session for pdu apc
  ✓ It adds login and password to pdu interface only if both are provided[login-password-True]
  ✓ It adds login and password to pdu interface only if both are provided[login--False]
  ✓ It adds login and password to pdu interface only if both are provided[-password-False]
  ✓ It adds login and password to pdu interface only if both are provided[--False]

tests/tests_ute_ca_worker/unittests/lib/test_ssh.py:

Ssh client:
  ✓ It returns ssh client when one ssh service exists
  ✓ It raises exception when two ssh services exists
  ✓ It raises exception when ssh service not exists

tests/tests_ute_ca_worker/unittests/lib/test_telnet.py:

New telnet:

  Read very eager with limit:
    ✓ It reads data with limit
    ✓ It stops reading if sock avail is false
    ✓ It raises eoferror

Telnet client:

  Close connection:
    ✓ It closes connection

  Host property:
    ✓ It returns host ip

  Open connection:
    ✓ It opens connection

  Port property:
    ✓ It returns host ip

  Read:
    ✓ It reads output

  Read until regexp:
    ✓ It reads until regexp
    ✓ It ignores prompts before valid data
    ✓ It returns positive status
    ✓ It returns negative status

  Set option callback:
    ✓ It negotiates window size
    ✓ It negotiate rejection of other option than window size

  Write:
    ✓ It writes given cmd

  Write bare:
    ✓ It writes given cmd

tests/tests_ute_ca_apiserver/apps/logger/test_logger_core.py:

Socket handler filter:
  ✓ It returns true if the log record matches the filtering criteria
  ✓ It returns false if the log record matches the filtering criteria

Socket logging manager:
  ✓ It adds socket handlers
  ✓ It removes socket handlers
  ✓ It raises key error if you try to remove unregistered handler
  ✓ It returns true if handler exist and false otherwise

tests/tests_ute_ca_agentctl/utils/logging/test_filters.py:

UcaTransportShellFilter:
  ✓ It filters out unwanted records[record0]
  ✓ It does not filter out wanted records[record0]
  ✓ It does not filter out wanted records[record1]

tests/tests_ute_ca_agentctl/utils/logging/test_formatters.py:

LoggingFormatter:
  ✓ It is a subclass of Formatter
  ✓ It calls format record method if extra in log record
  ✓ It follows standard formatting for regular records

Format record:
  ✓ It raises an error if rendarable class not registered

  ExecutionDebug:
    ✓ It formats execution debug with str content
    ✓ It formats execution debug with dict content
    ✓ It formats execution debug with exception content

  LogCancelCommand:
    ✓ It formats cancel commands output

  LogHighlightedMessage:
    ✓ It formats highlighted message

  LogInfoCommandOut:
    ✓ It formats info commands output

  LogRunCommandFinalState:
    ✓ It formats run commands final state

  LogRunCommandInit:
    ✓ It formats run commands init arguments

  LogTaskDagResult:
    ✓ It formats task dag log results

  HttpxResponse:
    ✓ It formats json response
    ✓ It formats text response

Log task dag result formatters:

  Message formatter:
    ✓ It formats message column

  Node formatter:
    ✓ It formats node info column

  Obj type formatter:
    ✓ It formats obj type column[Task-bold]
    ✓ It formats obj type column[Dag-bold yellow]

  Result formatter:
    ✓ It formats result column[Passed-bold green]
    ✓ It formats result column[Failed-bold red]
    ✓ It formats result column[Skipped-bold #7a807c]
    ✓ It formats result column[Scheduled-bold cyan]
    ✓ It formats result column[Retried-bold turquoise4]
    ✓ It formats result column[Running-bold bright magenta]
    ✓ It formats result column[Other-bold]

tests/tests_ute_ca_agentctl/utils/logging/test_handlers.py:

LoggingHandler:
  ✓ It is a subclass of RichHandler
  ✓ It uses the original RichHandler rendering for string messages
  ✓ It passes through non string objects

tests/tests_ute_ca_agentctl/utils/logging/test_helpers.py:

LogReceiver:

  Clean:
    ✓ It cleans the server and thread attributes[log receiver factory0]

  Get address:
    ✓ It returns the LoggingTCPServer address
    ✓ It raises an error when receiver not runing

  Is running:
    ✓ It shows if the LogReceiver is running[log receiver factory0]
    ✓ It shows if the LogReceiver is running[log receiver factory1]

  Start:
    ✓ It starts the LogReceiver
    ✓ It raises an error when receiver already running[log receiver factory0]

  Stop:
    ✓ It stops the LogReceiver[log receiver factory0]
    ✓ It raises an error when receiver not running

LoggingTCPServer:
  ✓ It is a subclass of socketserverTCPServer
  ✓ It sets the handler shutdown event on shutdown

Add file log:
  ✓ It adds file handler to the current logger

Catch errors:
  ✓ It handles any exception
  ✓ It handles http status exception
  ✓ It does nothing if no exception occured

Check if execution failed and log debug information:
  ✓ It calls apiserver and logs debug information if debug
  ✓ It calls apiserver and doesnt log debug information if no debug
  ✓ It prints detailed debug info about first failed task if no debug
  ✓ It prints relevant error message if no first failed task debug
  ✓ It prints worker stderr if worker failed

Create logs directory:
  ✓ It calls unlink and symlink to for all files
  ✓ It sends signal if there is already a file or dir in output dir

tests/tests_ute_ca/models/test_execution.py:

ExecutionDebug:

  Make pickle:
    ✓ It creates a pickled execution debug
    ✓ It installs pickling support for exceptions

tests/tests_ute_ca/models/test_provision.py:

Agent modes:

  Enum matches correct strings:
    ✓ It matches init
    ✓ It matches check
    ✓ It matches repair

Required state:

  Comparison methods:
    ✓ It compares properly between enum members
    ✓ It compares properly between enum members and proper strings
    ✓ It raises if string is not a member of the enum

  Members list and index:
    ✓ It returns members in proper order
    ✓ It returns proper index for enum member

tests/tests_ute_ca/models/test_testline.py:

Service:

  Addr validator:
    ✓ It should not touch the correct addr[fpfh-gf12-48-sc5g.sc5g-leg.krk-lab.nsn-rdnet
    ✓ It should not touch the correct addr[2-7-tl1022.vir.krk-lab.nsn-rdnet
    ✓ It should not touch the correct addr[192.99.99
    ✓ It should not touch the correct addr[1.1.1
    ✓ It should not touch the correct addr[FPFH-GK04-23-SC5G.sc5g-leg.krk-lab.nsn-rdnet
    ✓ It should raise exception for wrong addr format[192.99.319
    ✓ It should raise exception for wrong addr format[-2-7-tl1022.vir.krk-lab.nsn-rdnet
    ✓ It should raise exception for wrong addr format[192.99.
    ✓ It should raise exception for wrong addr format[]
    ✓ It should raise exception for wrong addr format[FPFH-GK04-23-SC5G.sc5g-leg.krk-lab.nsn-rdnet
    ✓ It should raise exception for wrong addr format[none]
    ✓ It should raise exception for wrong addr format[None]

    It should not touch the correct addr[1050:
      ✓ 5:600:300c:326b]

VmInterface:

  Name validator:
    ✓ It should not touch the correct name[eth5]
    ✓ It should not touch the correct name[eth999]
    ✓ It should raise exception for wrong name format[some random string]
    ✓ It should raise exception for wrong name format[eth1:2]
    ✓ It should raise exception for wrong name format[eth]

tests/tests_ute_ca_apiserver/models/test_execution_models.py:

Execution model:
  ✓ It has proper str representation
  ✓ It has proper repr

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/ocp_sw_update/test_callables.py:

Are images available:
  ✓ It returns true if all expected images are available
  ✓ It returns false if at least one image is not available

Check persistent volumes states:
  ✓ It reads all available persisten valumes
  ✓ It raises error if at least one persistent volume has incorrect state
  ✓ It raises error if read operation failed

Cleanup artifacts:
  ✓ It removes downloaded artifacts
  ✓ It raises error if remove operation failed

Copy onboarding app files:
  ✓ It copy onboarding file to image directory
  ✓ It raises error if copy operation failed

Create build dir:
  ✓ It creates working directory on controller
  ✓ It raises error if execution failed

Download ocp sw file:
  ✓ It downloads software
  ✓ It raises error if download operation failed

Download onboarding app:
  ✓ It downloads onboarding app
  ✓ It raises error if download failed

Is helm charts dir exist:
  ✓ It returns true if directory exists
  ✓ It returns false if directory does not exist

Is it vdu:
  ✓ It returns true if deployment has vdu
  ✓ It returns false if deployment does not has vdu

Load images:
  ✓ It executes script to load images
  ✓ It raises error if load image operation failed

Read available images:
  ✓ It reads available images on controller
  ✓ It removes hostname part from images
  ✓ It raises error if operation failed

Read images from onboarding app:
  ✓ It reads images from unpacked onboarding app
  ✓ It parses output to return only images urls
  ✓ It raises error if read operation failed

Select software:
  ✓ It selects vdu software
  ✓ It selects vcu software
  ✓ It raises error if not supported device provided

Start toolbox:
  ✓ It starts toolbox core via ssh
  ✓ It raises error if execution failed

Uninstall release:
  ✓ It executes helm to uninstall release[cnf]
  ✓ It executes helm to uninstall release[prerequisite]
  ✓ It executes helm to uninstall release[cluster-preparation]
  ✓ It supresses errors about not existing release
  ✓ It raises errors if helm command failes

Unpack helm charts:
  ✓ It unpacks helm charts
  ✓ It raises error if unpack operation failed

Unpack ocp sw file:
  ✓ It unzips ocp sw file
  ✓ It raises error if operation failed

Unpack onboarding app:
  ✓ It unpacks onboarding tgz file
  ✓ It raises error if unpack failed

Update charts permissions:
  ✓ It change owner for unpacked files
  ✓ It raises error if operation failed

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/ocp_sw_update/test_dag.py:

Create ocp sw update:
  ✓ It returns dag
  ✓ It has proper tasks

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/open_stack_sw_update/test_callables.py:

Load image:
  ✓ It should raise load image error when image load fails
  ✓ It loads image with verified image checksum

Removes stack:
  ✓ It removes stack

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/open_stack_sw_update/test_dag.py:

Create open stack sw update:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_classical_radio_sw_update/test_callables.py:

Is real radios available:
  ✓ It return false when no radios
  ✓ It return true when radios available

Wait for radio sw alarm:
  ✓ It returns false when all radios online
  ✓ It returns true when radio sw alarm found
  ✓ It raises exception when not all radios online and no radio sw alarm

Wait for radios to be detected:
  ✓ It raises exception when radio not detected
  ✓ It does not raise error when all radios detected

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_cus_commissioning/test_callables.py:

Cus executor config remote update:
  ✓ It executes update command
  ✓ It throws error when no matching regex

Run docker tgr:
  ✓ It executes shell commands for docker tgr

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_cus_commissioning/test_dag.py:

Create perform sim commissioning:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_ocp_deployment/test_callables.py:

Choose files to migrate and upload:
  ✓ It returns empty array when no files
  ✓ It returns proper tasks
  ✓ It returns all possible tasks

Unpack conversion app:
  ✓ It executes correct comamnds

Upload file to controller:
  ✓ It uploads vdu cnf proper dst
  ✓ It uploads cnf file
  ✓ It uploads cluster preparation file
  ✓ It uploads prerequisite file

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_ocp_deployment/test_commands.py:

Helm install command:
  ✓ It generates correct command

Cd helm chart command:
  ✓ It generates correct command
  ✓ It generates correct command vcu cnf

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_ocp_deployment/test_dag.py:

Create perform ocp deployments:
  ✓ It returns dag
  ✓ It has proper tree

Create perform ocp deplyment:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_ocp_vdu_commissioning/test_callables.py:

Activate scf:
  ✓ It activates scf

Check admin connection:
  ✓ It returns none if connection established
  ✓ It raises exception if connect failed

Check scf activation status:
  ✓ It checks scf activation status
  ✓ It raises exception if scf activation failed

Check scf upload status:
  ✓ It checks scf upload status
  ✓ It raises exception if scf upload failed

Check scf validation status:
  ✓ It checks scf validation status
  ✓ It raises exception if scf validation failed

Send scf to vdu:
  ✓ It sends scf to vdu

Validate scf:
  ✓ It validates scf

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_ocp_vdu_commissioning/test_dag.py:

Create perform vdu ocp commissioning subdag:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_sim_commissioning/test_callables.py:

Discover sim location:
  ✓ It discovers sim location

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_sim_commissioning/test_command.py:

Create directory on partition command:
  ✓ It generates proper command

Make symbolic link command:
  ✓ It generates proper command

Set domain id on device command:
  ✓ It generates proper command

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_sim_commissioning/test_dag.py:

Create perform sim commissioning:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_sm_commissioning/test_callables.py:

Check variable:
  ✓ It checks if variable is available and has proper value
  ✓ It raises error if variable has wrong value

Commission sm:
  ✓ It sends scfc file
  ✓ It pushes variable with positive result
  ✓ It pushes variable with negative result in case of exception

Is fsih:
  ✓ It returns true if fsih
  ✓ It returns false if not fsih

Is fsmf or asia:
  ✓ It returns true if fsih
  ✓ It returns true if asia
  ✓ It returns false if not fsmf

Select commissioning case:
  ✓ It selects halfrack tasks
  ✓ It selects fullrack master tasks
  ✓ It selects fullrack slave tasks

Set variable:
  ✓ It pushes variable

Verify adets py2:
  ✓ It verifies adets

Verify adets py3:
  ✓ It verifies adets

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_sm_commissioning/test_dag.py:

Create perform sm commissioning:
  ✓ It returns dag
  ✓ It has all tasks
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_vcu_commissioning/test_callables.py:

Callables:
  ✓ It sends scf file
  ✓ It waits for success scf upload status
  ✓ It raises exception when upload status not success
  ✓ It validates scf file
  ✓ It waits for success scf validation status
  ✓ It raises exception when validation status not success
  ✓ It activates scf file
  ✓ It waits for success scf activation status
  ✓ It raises exception when activation status not success
  ✓ It collects cu snapshot
  ✓ It waits for enabled operational state
  ✓ It raises exception when operational state not enabled

tests/tests_ute_ca_worker/unittests/dag/commissioned/perform_vcu_commissioning/test_dag.py:

Create perform vcu commissioning:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/shared/power_off_available_fbbps/test_callables.py:

Select fbbps operations:
  ✓ It returns no tasks if device is not system module
  ✓ It returns no tasks if device is not fsmf
  ✓ It disables both capacity units if available
  ✓ It disables the first capacity unit if only available
  ✓ It returns an empty list if no units are avaible

tests/tests_ute_ca_worker/unittests/dag/shared/power_off_available_fbbps/test_dag.py:

Create power off available fbbps on device dag:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/power_off_device/test_dag.py:

Create power off device subdag:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/ssh_only/power_on_and_check_ssh_services/test_callables.py:

Device pdu power on:
  ✓ It checks port status
  ✓ It powers on device

tests/tests_ute_ca_worker/unittests/dag/ssh_only/power_on_and_check_ssh_services/test_dag.py:

Create power on and check ssh services:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/commissioned/reboot_device/test_dag.py:

Create reboot device subdag:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_apiserver/apps/scheduler/test_core.py:

Scheduler:
  ✓ It sends to correct handler

tests/tests_ute_ca_apiserver/apps/scheduler/test_triggers.py:

AllPassedOrSkippedTriggerRule:
  ✓ It properly validates predecessors states[scenario0]
  ✓ It properly validates predecessors states[scenario1]
  ✓ It properly validates predecessors states[scenario2]
  ✓ It properly validates predecessors states[scenario3]

AllPassedTriggerRule:
  ✓ It properly validates predecessors states[scenario0]
  ✓ It properly validates predecessors states[scenario1]
  ✓ It properly validates predecessors states[scenario2]
  ✓ It properly validates predecessors states[scenario3]

AlwaysTriggerRule:
  ✓ It properly validates predecessors states[scenario0]
  ✓ It properly validates predecessors states[scenario1]
  ✓ It properly validates predecessors states[scenario2]
  ✓ It properly validates predecessors states[scenario3]

AnyFailedTriggerRule:
  ✓ It properly validates predecessors states[scenario0]
  ✓ It properly validates predecessors states[scenario1]
  ✓ It properly validates predecessors states[scenario2]
  ✓ It properly validates predecessors states[scenario3]

tests/tests_ute_ca_apiserver/apps/scheduler/test_websocket.py:

WebSocketReceiver:

  Receive:
    ✓ It raises exception when events ids does not match
    ✓ It returns event if events ids matches
    ✓ It raises exception if received not allowed event

  Run:
    ✓ It ends execution when websocket disconnect exception with code 1000 was raised
    ✓ It raises exception when websocket disconnect exception with code 1002 was raised
    ✓ It raises exception when send fails

WebSocketSender:
    ✓ It ends execution when websocket disconnect exception with code 1000 was raised
    ✓ It raises exception when websocket disconnect exception with code 1002 was raised
    ✓ It raises exception when send fails

  Send:
    ✓ It raises exception if ids does not match
    ✓ It sends json two times if ids match

tests/tests_ute_ca_worker/unittests/dag/shared/set_up_fbbps_on/test_callables.py:

Capacity unit pdu power on:
  ✓ It raises error if capacity unit does not have pdu
  ✓ It checks port status
  ✓ It powers on device

Select fbbps operations:
  ✓ It returns no tasks if device is not system module
  ✓ It returns no tasks if device is not fsmf
  ✓ It disables both capacity units for cloud f label if available
  ✓ It disables first capacity unit for cloud f label if only first available
  ✓ It returns empty list for cloud f if capacity unit are not available
  ✓ It enables first capacity unit for cloud fc if only first is available
  ✓ It disables second capacity unit for cloud fc if it is available
  ✓ It enables both capacity units for cloud fcc
  ✓ It returns empty list for 5G configuration without capacity units
  ✓ It enables first capacity unit for 5G configuration if it is available
  ✓ It enables both capacity units for 5G configuration if it is available

tests/tests_ute_ca_worker/unittests/dag/shared/set_up_fbbps_on/test_dag.py:

Create set up fbbps on device dag:
  ✓ It creates a dag
  ✓ It has proper tree

tests/tests_ute_ca_apiserver/shared/test_nested_dict.py:

NestedDict:

  Update nested:
    ✓ It raises type error when second variable is not a dict
    ✓ It raises key error when key already exists
    ✓ It raises type error when existing key is not a dict
    ✓ It adds new key

tests/tests_ute_ca_worker/unittests/dag/commissioned/shared/test_callables.py:

Is file available:
  ✓ It returns true if file exist
  ✓ It returns false if file does not exist

Upload file to device:
  ✓ It uploads file
  ✓ It uploads and signs file

tests/tests_ute_ca_worker/unittests/dag/shared/test_callables.py:

Capacity unit pdu power off:
  ✓ It raises error if capacity unit does not have pdu
  ✓ It checks port status
  ✓ It powers off device

Collect snapshot from sm:
  ✓ It collects snapshot from sm

Cus executor config update:
  ✓ It executes update command
  ✓ It throws error when no matching regex

Discover partitions:
  ✓ It returns fs1 as active partition
  ✓ It returns fs2 as active partition

Download sw file:
  ✓ It downloads file from repository
  ✓ It raises error if more than one file found
  ✓ It adds subpath when provided

Is asik sim:
  ✓ It returns true if is asik sim
  ✓ It returns false if is not asik sim

Is fsmh or fsih:
  ✓ It returns true if system module is fsmf
  ✓ It returns true if simulator module is fsmf
  ✓ It returns true if simulator module is fsih
  ✓ It returns true if system module is fsih
  ✓ It returns false if system module is asik

Is non vm device with ssh:
  ✓ It determines if device is not a vm and has ssh[device0-True]
  ✓ It determines if device is not a vm and has ssh[device1-False]
  ✓ It determines if device is not a vm and has ssh[device2-False]

Is ssh down:
  ✓ It raises exception when ssh is up

Is ssh up:
  ✓ It raises exception when ssh is down

Parse config yaml:
  ✓ It parses config yaml properly with single hook
  ✓ It parses config yaml properly with multiple hooks
  ✓ It parses config yaml properly without hooks
  ✓ It raises error when variant does not exist
  ✓ It reads proper variant configuration
  ✓ It reads variant metadata
  ✓ It parses properly fullrack config[1-slave-2]
  ✓ It parses properly fullrack config[2-master-1]
  ✓ It parses properly fullrack config[3-None-None]
  ✓ It parses properly fullrack config[4-master-5]
  ✓ It parses properly fullrack config[5-slave-4]
  ✓ It returns none if file doesnt exist
  ✓ It raises error when config is invalid[file path0]
  ✓ It raises error when config is invalid[file path1]
  ✓ It raises error when config is invalid[file path2]
  ✓ It raises error when config is invalid[file path3]

Power off via pdu:
  ✓ It powers off ports

Power on via pdu:
  ✓ It powers on ports

Reboot via pdu:
  ✓ It resets ports

tests/tests_ute_ca_worker/unittests/dag/shared/test_models.py:

Config file:

  Default variant:
    ✓ It returns default variant
    ✓ It raises config yaml variant missing error
    ✓ It raises config yaml variant count mismatch error

  Get variant:
    ✓ It returns specific variant
    ✓ It raises config yaml variant missing error
    ✓ It raises config yaml variant count mismatch error
    ✓ It parses cus correctly

Node:

  Get file:
    ✓ It returns requested file
    ✓ It raises config yaml file missing error
    ✓ It raises config yaml file count mismatch error

Variant:

  Get fullrack:
    ✓ It returns requested fullrack if exist
    ✓ It returns none if fullrack for requested node does not exist

  Get node:
    ✓ It returns requested node
    ✓ It raises config yaml node missing error
    ✓ It raises config yaml variant count mismatch error

tests/tests_ute_ca_worker/unittests/dag/ssh_only/shared/test_callables.py:

Check ssh service:
  ✓ It executes proper command
  ✓ It raises exception if device is unreachable

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/shared/test_callables.py:

Are checksums equal:
  ✓ It returns true if checksums are the same
  ✓ It returns false if checksums are different

Compute adler32 for partition:
  ✓ It calculates checksums on device
  ✓ It returns empty list in case of exception

Copy logs from tmp dir:
  ✓ It copies logs from tmp dir

Download yaft:
  ✓ It should download yaft

Install yaft:
  ✓ It installs yaft

Is software in cache:
  ✓ It should return false if software directory doesnt exists
  ✓ It should return false if software package is missing
  ✓ It should return true if software is in cache

Remove dirs:
  ✓ It removes all provided directories

Restore authorized keys:
  ✓ It restores authorized keys

Run yaft:
  ✓ It should run yaft

Unzip sw:
  ✓ It unzips software to random temp directory

Upload adler32 binary:
  ✓ It uploads proper binary to device[armv7l]
  ✓ It uploads proper binary to device[mips64]
  ✓ It uploads proper binary to device[x86 64]

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/shared/test_commands.py:

Set active partition command:
  ✓ It generates correct command

tests/tests_ute_ca_worker/unittests/dag/ssh_only/test_ssh_only.py:

Create check ssh dag:
  ✓ It returns dag
  ✓ It returns one task per device
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/ssh_only/ssh_only_on_device/test_callables.py:

Is connected to pdu:
  ✓ It returns true for devices which are connected to pdu
  ✓ It returns false for devices not connected to pdu

tests/tests_ute_ca_worker/unittests/dag/ssh_only/ssh_only_on_device/test_dag.py:

Create ssh only on device:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/test_callables.py:

Create hook configuration file:
  ✓ It writes data to file

Is hook present:
  ✓ It returns true if hook present
  ✓ It return false if hook not present

Is post sw uploaded hook present:
  ✓ It returns true if hook present
  ✓ It returns fale if hook not present
  ✓ It returns false if only commission hook present

Is topology config present:
  ✓ It returns true if file present
  ✓ It returns false if file not present

Resolve topology configs dir:
  ✓ It returns proper path

Select type of sw update:
  ✓ It returns perform classical sw update if only system module is available
  ✓ It returns perform open stack sw update if only controller is available
  ✓ It returns perform ocp sw update tasks if ocp controller is available
  ✓ It returns perform cloud and classical sw update if both controller and system module are available

tests/tests_ute_ca_worker/unittests/dag/sw_uploaded/test_main.py:

Create sw uploaded:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca/test_exception_handlers.py:

Http exception handler:
  ✓ It returns jsonresponse with header
  ✓ It returns jsonresponse without header

Parse exception recursively:
  ✓ It returns exception dict if exception is given
  ✓ It returns empty dict if no original exception is given
  ✓ It returns original exception from nested exception
  ✓ It removes empty keys from exception dict

tests/tests_ute_ca/test_exceptions.py:

NestedHTTPException:
  ✓ It uses response str representation if json decode failed

tests/tests_ute_ca/test_testline.py:

Build model:
  ✓ It returns proper branch[SBTS00 ENB 9999 220426 000007-SBTS00]
  ✓ It returns proper branch[4.0.20500-4
  ✓ It returns proper branch[5G 4.3.20500-4
  ✓ It returns proper branch[vDUCNF00 0.300
  ✓ It returns proper branch[vCUCNF00 0.300
  ✓ It returns proper branch[pDU22R2 14.400
  ✓ It returns proper branch[CUVNF22R2 14.200
  ✓ It returns proper branch[WTS 4091130.8 4.0
  ✓ It returns proper branch[CUS 1.0.REL.220420.6-1
  ✓ It returns proper branch[5G21B 12.400.1860-12

Testline:
  ✓ It properly initializes

tests/tests_ute_ca_agentctl/test_cli.py:

App:
  ✓ It runs ute ca agentctl

tests/tests_ute_ca_agentctl/test_legacy_cli.py:

Check:
  ✓ It supports no options
  ✓ It supports some options

Init:
  ✓ It runs with just build and label
  ✓ It runs with just build and label long
  ✓ It requires build
  ✓ It requires label
  ✓ It supports extra options
  ✓ It sets variant to one found in CM TAGS
  ✓ It raises error if more than one variant in CM TAGS

Repair:
  ✓ It runs with just label
  ✓ It runs with just label long
  ✓ It requires label
  ✓ It supports extra options

tests/tests_ute_ca_apiserver/test_events.py:

On startup:
  ✓ It starts the scheduler

Shutdown:
  ✓ It stops the scheduler

tests/tests_ute_ca_manager/utils/tl_config/test_importer.py:

ConfigImporter:
  ✓ It raises an error when configuration file not found
  ✓ It raises an error when spec cannot be created
  ✓ It imports testline configuration[testline configuration0]
  ✓ It imports testline configuration[testline configuration1]
  ✓ It imports testline configuration[testline configuration2]
  ✓ It imports testline configuration[testline configuration3]
  ✓ It imports testline configuration[testline configuration4]
  ✓ It imports testline configuration[testline configuration5]
  ✓ It imports testline configuration[testline configuration6]
  ✓ It imports testline configuration[testline configuration7]
  ✓ It imports testline configuration[testline configuration8]
  ✓ It imports testline configuration[testline configuration9]
  ✓ It imports testline configuration[testline configuration10]
  ✓ It imports testline configuration[testline configuration11]

tests/tests_ute_ca_manager/utils/tl_config/test_parser.py:

TestlineConfigParser:

  Parse:
    ✓ It uses 4g parser for ute config configurations[testline configuration0]
    ✓ It uses 4g parser for ute config configurations[testline configuration1]
    ✓ It uses 4g parser for ute config configurations[testline configuration2]
    ✓ It uses 4g parser for ute config configurations[testline configuration3]
    ✓ It uses 4g parser for ute config configurations[testline configuration4]
    ✓ It uses 4g parser for ute config configurations[testline configuration5]
    ✓ It uses 4g parser for ute config configurations[testline configuration6]
    ✓ It uses 4g parser for ute config configurations[testline configuration7]
    ✓ It uses 4g parser for ute config configurations[testline configuration8]
    ✓ It uses 4g parser for ute config configurations[testline configuration9]
    ✓ It uses 4g parser for ute config configurations[testline configuration10]
    ✓ It uses 4g parser for ute config configurations[testline configuration11]
    ✓ It uses 5g parser for testline configurations[testline configuration0]
    ✓ It uses 5g parser for testline configurations[testline configuration1]
    ✓ It uses 5g parser for testline configurations[testline configuration2]
    ✓ It uses 5g parser for testline configurations[testline configuration3]
    ✓ It uses 5g parser for testline configurations[testline configuration4]
    ✓ It uses 5g parser for testline configurations[testline configuration5]
    ✓ It uses 5g parser for testline configurations[testline configuration6]
    ✓ It uses 5g parser for testline configurations[testline configuration7]
    ✓ It uses 5g parser for testline configurations[testline configuration8]
    ✓ It uses 5g parser for testline configurations[testline configuration9]
    ✓ It uses 5g parser for testline configurations[testline configuration10]
    ✓ It uses 5g parser for testline configurations[testline configuration11]
    ✓ It uses 5g parser for testline configurations[testline configuration12]
    ✓ It uses 5g parser for testline configurations[testline configuration13]
    ✓ It uses 5g parser for testline configurations[testline configuration14]
    ✓ It uses 5g parser for testline configurations[testline configuration15]
    ✓ It uses 5g parser for testline configurations[testline configuration16]
    ✓ It uses 5g parser for testline configurations[testline configuration17]
    ✓ It uses 5g parser for testline configurations[testline configuration18]
    ✓ It uses 5g parser for testline configurations[testline configuration19]
    ✓ It uses 5g parser for testline configurations[testline configuration20]
    ✓ It raises error if unknown class is provided

tests/tests_ute_ca_manager/utils/tl_config/test_parser_4g.py:

Config4gParser:
    ✓ It parses ute config configurations properly[testline configuration0]
    ✓ It parses ute config configurations properly[testline configuration1]
    ✓ It parses ute config configurations properly[testline configuration2]
    ✓ It parses ute config configurations properly[testline configuration3]
    ✓ It parses ute config configurations properly[testline configuration4]
    ✓ It parses ute config configurations properly[testline configuration5]
    ✓ It parses ute config configurations properly[testline configuration6]
    ✓ It parses ute config configurations properly[testline configuration7]
    ✓ It parses ute config configurations properly[testline configuration8]
    ✓ It parses ute config configurations properly[testline configuration9]
    ✓ It parses ute config configurations properly[testline configuration10]
    ✓ It parses ute config configurations properly[testline configuration11]
    ✓ It raises error if system module cannot be parsed[testline configuration0]
    ✓ It raises error if fsmf capacity unit cannot be parsed[testline configuration0]
    ✓ It raises error if airscale capacity unit cannot be parsed[testline configuration0]

tests/tests_ute_ca_manager/utils/tl_config/test_parser_5g.py:

Config5gParser:
    ✓ It parses taf config configurations properly[testline configuration0]
    ✓ It parses taf config configurations properly[testline configuration1]
    ✓ It parses taf config configurations properly[testline configuration2]
    ✓ It parses taf config configurations properly[testline configuration3]
    ✓ It parses taf config configurations properly[testline configuration4]
    ✓ It parses taf config configurations properly[testline configuration5]
    ✓ It parses taf config configurations properly[testline configuration6]
    ✓ It parses taf config configurations properly[testline configuration7]
    ✓ It parses taf config configurations properly[testline configuration8]
    ✓ It parses taf config configurations properly[testline configuration9]
    ✓ It parses taf config configurations properly[testline configuration10]
    ✓ It parses taf config configurations properly[testline configuration11]
    ✓ It parses taf config configurations properly[testline configuration12]
    ✓ It parses taf config configurations properly[testline configuration13]
    ✓ It parses taf config configurations properly[testline configuration14]
    ✓ It parses taf config configurations properly[testline configuration15]
    ✓ It parses taf config configurations properly[testline configuration16]
    ✓ It parses taf config configurations properly[testline configuration17]
    ✓ It parses taf config configurations properly[testline configuration18]
    ✓ It parses taf config configurations properly[testline configuration19]
    ✓ It parses taf config configurations properly[testline configuration20]
    ✓ It parses taf config cloud multi du properly[testline configuration0]
    ✓ It parses taf config cus without connections properly[testline configuration0]
    ✓ It parses taf config multi cus properly[testline configuration0]
    ✓ It parses taf config aic multi gnb multi du properly[testline configuration0]
    ✓ It parses taf config aic shared controller properly[testline configuration0]
    ✓ It parses taf config aic no du properly[testline configuration0]
    ✓ It parses taf config aic mixed cloud classical enb properly[testline configuration0]
    ✓ It parses real enb with system module param properly[testline configuration0]
    ✓ It parses testline with 2 gnbs as single list properly[testline configuration0]
    ✓ It parses testline with enb and nb properly[testline configuration0]
    ✓ It parses testline with enb and bts2g properly[testline configuration0]

tests/tests_ute_ca_worker/unittests/dag/tools_installation/tools_installation/test_callables.py:

Is wts installation needed:
  ✓ It return true if simulator device is available
  ✓ It return false if simulator device is not available

tests/tests_ute_ca_worker/unittests/dag/tools_installation/tools_installation/test_dag.py:

Create tool installation:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/test_cli.py:

App:
  ✓ It calls provision

Run:
  ✓ It calls typer run

tests/tests_ute_ca_worker/unittests/test_provision.py:

Provision:
  ✓ It calls all methods for pass scenario
  ✓ It calls all methods for fail scenario

tests/tests_ute_ca/utils/test_asyncio.py:

Sync to async:
  ✓ It returns an awaitable coroutine

tests/tests_ute_ca/utils/test_checksum.py:

Async calc sha256sum:
  ✓ It calculates the checksum of a file

Calc sha256sum:
  ✓ It calculates the checksum of a file

tests/tests_ute_ca/utils/test_config.py:

Utecaconfig:
  ✓ It reads config if path exists
  ✓ It checks if section definition exists[apiserver-True]
  ✓ It checks if section definition exists[manager-True]
  ✓ It raises an error if section definition does not exist
  ✓ It reads the specified config section
  ✓ It returns none if section cannot be read
  ✓ It validates the read section[apiserver-values0]
  ✓ It validates the read section[apiserver-values1]
  ✓ It validates the read section[apiserver-values2]
  ✓ It validates the read section[apiserver-values3]
  ✓ It validates the read section[manager-values4]
  ✓ It validates the read section[manager-values5]
  ✓ It validates the read section[manager-values6]
  ✓ It validates the read section[manager-values7]
  ✓ It creates new config section

tests/tests_ute_ca/utils/test_enum.py:

AEnum:

  Hasmember:
    ✓ It checks if the argument is member of the enum

Merge enums:
  ✓ It merges multiple enums
  ✓ It raises value error if not at least two elements to merge are provided
  ✓ It raises type error if not all arguments are enums
  ✓ It raises key error if there are overlapping enumaration entries

tests/tests_ute_ca/utils/test_network.py:

Get default network interface addr:
  ✓ It returns the default network interface IP

tests/tests_ute_ca/utils/test_systemd.py:

HTTPResponseReadinessProbe:

  Execute:
    ✓ It passes if the url starts responding
    ✓ It fails after reaching timeout

  Init:
    ✓ It requires a url

ReadinessProbe:
  ✓ It defines an abstract
  ✓ It enforces the execute method

SystemdNotifier:
  ✓ It is a subclass of Thread
  ✓ It defines a run method

  Init:
    ✓ It requires at least one readiness probe[readiness probes0]
    ✓ It requires at least one readiness probe[readiness probes1]
    ✓ It requires at least one readiness probe[readiness probes2]
    ✓ It requires the notify socket to be set[True]
    ✓ It requires the notify socket to be set[False]

  Run:
    ✓ It sends readiness notification to systemd if all probes pass
    ✓ It sends error notification to systemd if any probe fails[probe results0]
    ✓ It sends error notification to systemd if any probe fails[probe results1]
    ✓ It sends error notification to systemd if any probe fails[probe results2]

SystemdReadinessProbe:

  Execute:
    ✓ It passes if the service is active
    ✓ It fails after reaching timeout
    ✓ It exits if non failed state changes to failed

  Init:
    ✓ It requires a service name

tests/tests_ute_ca_agentctl/utils/test_typer.py:

Typer command:
  ✓ It allows simple registration of classes as Typer commands

tests/tests_ute_ca_apiserver/utils/test_client.py:

ManagerClient:

  Get:
    ✓ It calls get properly
    ✓ It raises apiresponse exception on http error

  Post:
    ✓ It calls post properly
    ✓ It raises apiresponse exception on http error

  Put:
    ✓ It calls put properly
    ✓ It raises apiresponse exception on http error

  Server address:
    ✓ It returns the server address
    ✓ It raises an error when config path does not exist
    ✓ It raises an error when config section does not exist

tests/tests_ute_ca_manager/utils/test_build.py:

Build:

  Get latest artifact build:
    ✓ It raises exception when artifact list is empty
    ✓ It should return latest artifact

  Get related build:
    ✓ It should return related build
    ✓ It should raise exception when artifact list is empty

tests/tests_ute_ca_manager/utils/test_downloader.py:

ConfigDownloader:
  ✓ It returns the correct path
  ✓ It returns the correct path for nested subpath
  ✓ It uses cwd by default
  ✓ It responds to subpath not found error
  ✓ It responds to server error
  ✓ It responds to shell execution error

tests/tests_ute_ca_manager/utils/test_logger.py:

Configure logging:
  ✓ It configures logging

Configure loguru:
  ✓ It configures loguru logger

tests/tests_ute_ca_manager/utils/test_velocity.py:

VelocityReservationHandler:
  ✓ It retrieves the local environment variables over ssh
  ✓ It retrieves the velocity reservation
  ✓ It raises en error if credentials are missing[env vars0]
  ✓ It raises en error if credentials are missing[env vars1]
  ✓ It raises en error if credentials are missing[env vars2]
  ✓ It parses cm tags
  ✓ It creates the reservation
  ✓ It releases reservation before reservation
  ✓ It releases the reservation

tests/tests_ute_ca_worker/unittests/utils/test_client.py:

DagApiClient:

  Get:
    ✓ It sends request to get data about dag

  Get all:
    ✓ It sends request to get data about all dags

  Register:
    ✓ It sends proper registration request for root dag
    ✓ It sends proper registration request for subdag

TaskApiClient:

  Change to failed:
    ✓ It changes task to failed

  Change to passed:
    ✓ It changes task to passed

  Change to schedule:
    ✓ It changes task to scheduled

  Get to schedule:
    ✓ It sends request to get tasks to schedule

WorkerApiClient:

  Change to failed:
    ✓ It changes worker status to failed

  Change to passed:
    ✓ It changes worker status to passed

  Get config:
    ✓ It returns worker configuration

  Register:
    ✓ It creates proper registration content
    ✓ It raises error if response is incorrect

  Send heartbeat:
    ✓ It sends worker heartbeat

tests/tests_ute_ca_worker/unittests/utils/test_files.py:

Calculate md5:
  ✓ It calculates md5 checksum correctly
  ✓ It works with empty file
  ✓ It raises MD5CalculationError if error occurs

Checksum:
  ✓ It calculates md5 when hash algorithm is not specified
  ✓ It calculates hashes correctly with given algorithms[openssl md5-098f6bcd4621d373cade4e832627b4f6]
  ✓ It calculates hashes correctly with given algorithms[openssl sha1-a94a8fe5ccb19ba61c4c0873d391e987982fbbd3]
  ✓ It calculates hashes correctly with given algorithms[openssl sha224-90a3ed9e32b2aaf4c61c410eb925426119e1a9dc53d4286ade99a809]
  ✓ It calculates hashes correctly with given algorithms[openssl sha256-9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08]
  ✓ It calculates hashes correctly with given algorithms[openssl sha384-768412320f7b0aa5812fce428dc4706b3cae50e02a64caa16a782249bfe8efc4b7ef1ccb126255d196047dfedf17a0a9]
  ✓ It calculates hashes correctly with given algorithms[openssl sha512-ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff]
  ✓ It calculates hashes correctly with given algorithms[blake2b-a71079d42853dea26e453004338670a53814b78137ffbed07603a41d76a483aa9bc33b582f77d30a65e6f29a896c0411f38312e1d66e0bf16386c86a89bea572]
  ✓ It calculates hashes correctly with given algorithms[openssl sha3 224-3797bf0afbbfca4a7bbba7602a2b552746876517a7f9b7ce2db0ae7b]
  ✓ It calculates hashes correctly with given algorithms[openssl sha3 256-36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80]
  ✓ It calculates hashes correctly with given algorithms[openssl sha3 384-e516dabb23b6e30026863543282780a3ae0dccf05551cf0295178d7ff0f1b41eecb9db3ff219007c4e097260d58621bd]
  ✓ It calculates hashes correctly with given algorithms[openssl sha3 512-9ece086e9bac491fac5c1d1046ca11d737b92a2b2ebd93f005d7b710110c0a678288166e7fbe796883a4f2e9b3ca9f484f521d0ce464345cc1aec96779149c14]
  ✓ It raises TypeError with shake128 and shake256[openssl shake 128]
  ✓ It raises TypeError with shake128 and shake256[openssl shake 256]
  ✓ It raises FileNotFoundError if file does not exist

tests/tests_ute_ca_worker/unittests/utils/test_logger.py:

Configure logging:
  ✓ It configures logging

Configure loguru:
  ✓ It configures loguru logger

tests/tests_ute_ca_worker/unittests/utils/test_manager.py:

ComponentsManager:

  Shutdown:
    ✓ It set stop signal
    ✓ It sends end event

  Start:
    ✓ It starts all components
    ✓ It registers signal to shutdown components

tests/tests_ute_ca_worker/unittests/utils/test_validators.py:

WorkerConnectionCheck:
  ✓ It routes connection check event successfully
  ✓ It logs connection failed error if connection cannot be established

Ensure aria service is available:
  ✓ It does nothing when aria can started
  ✓ It raises exception when aria cannot be started

Ensure config dir exists:
  ✓ It raises exception when config dir does not exist
  ✓ It does nothing when config dir exists

Ensure connectivity to apiserver api:
  ✓ It does nothing if connection to api works
  ✓ It logs an eror if connection to api doesnt work

Ensure working directory exists:
  ✓ It raises exception when config dir does not exist
  ✓ It does nothing when config dir exists

tests/tests_ute_ca_worker/unittests/utils/test_worker.py:

Register worker:
  ✓ It registers worker

Setup worker configuration:
  ✓ It setups worker configuration

tests/tests_ute_ca_worker/unittests/dag/shared/wait_for_states/test_callables.py:

Is it system module:
  ✓ It returns true if system module
  ✓ It returns false if not system module

Is it vcu:
  ✓ It returns true if vcu
  ✓ It returns false if not vcu

Select cell technologies:
  ✓ It selects correct tasks[bts info0-expected output0]
  ✓ It selects correct tasks[bts info1-expected output1]
  ✓ It selects correct tasks[bts info2-expected output2]

Verify bts state classical:
  ✓ It passes when correct[call parameters0-bts info0]
  ✓ It raises error when states are not correct[call parameters0-bts info0]
  ✓ It raises timeout error

Verify cells states classical:
  ✓ It passes when correct[call parameters0-bts info0]
  ✓ It passes when correct[call parameters1-bts info1]
  ✓ It raises error when states are not correct[call parameters0-bts info0]
  ✓ It raises error when states are not correct[call parameters1-bts info1]
  ✓ It raises error when cells empty[call parameters0-bts info0]
  ✓ It raises error when cells empty[call parameters1-bts info1]
  ✓ It raises timeout error
  ✓ It raises ValueError when procedural status or barring status and not technology NR

Verify cells states cloud:
  ✓ It passes when correct
  ✓ It raises error when states are not correct
  ✓ It raises timeout error

Verify f1 links:
  ✓ It passes when correct
  ✓ It raises error when du nr mismatch
  ✓ It raises timeout error

Verify rus states classical:
  ✓ It passes when correct[call parameters0-bts info0]
  ✓ It raises error when states are not correct[call parameters0-bts info0]
  ✓ It raises error when rmods empty
  ✓ It raises timeout error

Verify rus states cloud:
  ✓ It passes when correct
  ✓ It raises error when states are not correct
  ✓ It raises timeout error
  ✓ It retries after error

tests/tests_ute_ca_worker/unittests/dag/shared/wait_for_states/test_dag.py:

Create verify cell states classical dag:
  ✓ It returns dag
  ✓ It has proper tree

Create wait for states classical dag:
  ✓ It returns dag
  ✓ It has proper tree

Create wait for states cloud dag:
  ✓ It returns dag
  ✓ It has proper tree

Create wait for states dag:
  ✓ It returns dag
  ✓ It has proper tree

tests/tests_ute_ca_worker/unittests/dag/tools_installation/wts_installation/test_callables.py:

Copy wts config:
  ✓ It copies wts config to directory where wts is installed

Is iphy available:
  ✓ It raises error if testline does not have simulator
  ✓ It raises error if testline has more than one simulator
  ✓ It returns true if testline has iphy simulator
  ✓ It returns false if testline has airphone simulator

Is wts config available:
  ✓ It returns true if wts config is available
  ✓ It returns false if wts config is not available

Link wts package:
  ✓ It creates symbolic link to latest directory

Unpack wts package:
  ✓ It creates wts directory
  ✓ It unpacks wts package
  ✓ It returns path to extracted wts package

tests/tests_ute_ca_worker/unittests/dag/tools_installation/wts_installation/test_dag.py:

Create wts installation:
  ✓ It returns dag
  ✓ It has proper tree

===================================================================================== warnings summary =====================================================================================
../../../.pyenv/versions/3.9.2/envs/ute-ca/lib/python3.9/site-packages/yapf/__init__.py:35
  /home/adasiak/.pyenv/versions/3.9.2/envs/ute-ca/lib/python3.9/site-packages/yapf/__init__.py:35: PendingDeprecationWarning: lib2to3 package is deprecated and may not be able to parse Python 3.10+
    from lib2to3.pgen2 import tokenize

tests/tests_ute_ca_apiserver/crud/test_execution_crud.py::describe_show_execution_info::it_raises_does_not_exist_exception
  /home/adasiak/.pyenv/versions/3.9.2/lib/python3.9/unittest/mock.py:2105: RuntimeWarning: coroutine '_monitor_pending_state' was never awaited
    self.name = name

tests/tests_ute_ca_apiserver/apps/scheduler/test_websocket.py::describe_WebSocketSender::describe_run::it_raises_exception_when_websocket_disconnect_exception_with_code_1002_was_raised
  /home/adasiak/.pyenv/versions/3.9.2/lib/python3.9/enum.py:360: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited
    return cls.__new__(cls, value)

tests/tests_ute_ca_apiserver/apps/scheduler/test_websocket.py::describe_WebSocketSender::describe_run::it_raises_exception_when_websocket_disconnect_exception_with_code_1002_was_raised
tests/tests_ute_ca_apiserver/apps/scheduler/test_websocket.py::describe_WebSocketSender::describe_run::it_raises_exception_when_send_fails
  /home/adasiak/uca/naa/ute-ca/ute_ca_apiserver/apps/scheduler/websocket.py:81: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited
    self.worker_queue.task_done()

tests/tests_ute_ca_apiserver/apps/scheduler/test_websocket.py::describe_WebSocketSender::describe_run::it_raises_exception_when_send_fails
  /home/adasiak/.pyenv/versions/3.9.2/lib/python3.9/unittest/mock.py:2059: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited
    setattr(_type, entry, MagicProxy(entry, self))

tests/tests_ute_ca_apiserver/apps/scheduler/test_websocket.py::describe_WebSocketSender::describe_send::it_sends_json_two_times_if_ids_match
  /home/adasiak/uca/naa/ute-ca/ute_ca_apiserver/apps/scheduler/websocket.py:72: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited
    self.worker_queue.task_done()

tests/tests_ute_ca_worker/unittests/dag/shared/set_up_fbbps_on/test_callables.py::describe_select_fbbps_operations::it_enables_first_capacity_unit_for_5G_configuration_if_it_is_available
  /home/adasiak/.pyenv/versions/3.9.2/lib/python3.9/copy.py:253: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited
    memo[id(memo)].append(x)

-- Docs: https://docs.pytest.org/en/stable/warnings.html

----------- coverage: platform linux, python 3.9.2-final-0 -----------
Name                                                                            Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------------------------------------
ute_ca/__init__.py                                                                  0      0   100%
ute_ca/cli/__init__.py                                                              0      0   100%
ute_ca/cli/apiserver.py                                                            15      0   100%
ute_ca/cli/base.py                                                                 10      0   100%
ute_ca/cli/main.py                                                                  9      0   100%
ute_ca/cli/manager.py                                                              15      0   100%
ute_ca/constant.py                                                                  1      0   100%
ute_ca/defaults.py                                                                 10      0   100%
ute_ca/exception_handlers.py                                                       20      0   100%
ute_ca/exceptions.py                                                               26      0   100%
ute_ca/models/__init__.py                                                           0      0   100%
ute_ca/models/core.py                                                               3      0   100%
ute_ca/models/events.py                                                           100      1    99%   66
ute_ca/models/execution.py                                                         93      0   100%
ute_ca/models/helpers.py                                                           11      0   100%
ute_ca/models/provision.py                                                         39      4    90%   33, 38, 43, 48
ute_ca/models/task.py                                                              12      0   100%
ute_ca/models/testline.py                                                         345      2    99%   710-711
ute_ca/shared/__init__.py                                                           0      0   100%
ute_ca/shared/event_types.py                                                       29      0   100%
ute_ca/shared/logger.py                                                            15     11    27%   7-18
ute_ca/shared/states.py                                                            17      0   100%
ute_ca/shared/task.py                                                              15      0   100%
ute_ca/utils/__init__.py                                                            0      0   100%
ute_ca/utils/asyncio.py                                                            33      0   100%
ute_ca/utils/checksum.py                                                           20      0   100%
ute_ca/utils/config.py                                                             66      2    97%   61, 151
ute_ca/utils/enum.py                                                               25      2    92%   31, 66
ute_ca/utils/network.py                                                             9      2    78%   19-20
ute_ca/utils/systemd.py                                                            57      0   100%
ute_ca/utils/testline.py                                                            3      0   100%
ute_ca_agentctl/__init__.py                                                         1      0   100%
ute_ca_agentctl/cli.py                                                             37      0   100%
ute_ca_agentctl/commands/__init__.py                                                0      0   100%
ute_ca_agentctl/commands/base.py                                                   23      0   100%
ute_ca_agentctl/commands/models.py                                                 14      0   100%
ute_ca_agentctl/commands/provision.py                                             150      8    95%   51-52, 90, 138, 169, 192, 199, 281
ute_ca_agentctl/commands/signals.py                                                44      0   100%
ute_ca_agentctl/exceptions.py                                                       8      0   100%
ute_ca_agentctl/legacy_cli.py                                                      44      0   100%
ute_ca_agentctl/models/__init__.py                                                  0      0   100%
ute_ca_agentctl/models/logging.py                                                  48      0   100%
ute_ca_agentctl/utils/__init__.py                                                   0      0   100%
ute_ca_agentctl/utils/logging/__init__.py                                           0      0   100%
ute_ca_agentctl/utils/logging/filters.py                                            7      0   100%
ute_ca_agentctl/utils/logging/formatters.py                                       170      0   100%
ute_ca_agentctl/utils/logging/handlers.py                                          36     17    53%   51-67
ute_ca_agentctl/utils/logging/helpers.py                                          138      4    97%   64-65, 68, 257
ute_ca_agentctl/utils/typer.py                                                     12      0   100%
ute_ca_apiserver/__init__.py                                                        0      0   100%
ute_ca_apiserver/apps/__init__.py                                                   0      0   100%
ute_ca_apiserver/apps/logger/__init__.py                                            0      0   100%
ute_ca_apiserver/apps/logger/core.py                                               33      4    88%   27-29, 88
ute_ca_apiserver/apps/scheduler/__init__.py                                         0      0   100%
ute_ca_apiserver/apps/scheduler/core.py                                            71     13    82%   113-129, 141, 197-198
ute_ca_apiserver/apps/scheduler/events.py                                          29      0   100%
ute_ca_apiserver/apps/scheduler/exceptions.py                                       8      0   100%
ute_ca_apiserver/apps/scheduler/handlers/__init__.py                                0      0   100%
ute_ca_apiserver/apps/scheduler/handlers/core.py                                   35      1    97%   5
ute_ca_apiserver/apps/scheduler/handlers/dag.py                                   128     11    91%   10, 147, 294-309, 343
ute_ca_apiserver/apps/scheduler/handlers/task.py                                  264     61    77%   13, 65, 133-136, 153-157, 169-177, 190, 256, 265, 302, 304, 318-321, 326-327, 400-401, 421, 423, 438-439, 479, 488-494, 503-506, 525, 534-537, 586-592, 599, 620-621
ute_ca_apiserver/apps/scheduler/handlers/variable.py                               43      3    93%   8, 33-34
ute_ca_apiserver/apps/scheduler/handlers/worker.py                                 41      4    90%   6, 36-38
ute_ca_apiserver/apps/scheduler/handlers/xcom.py                                   62      3    95%   7, 63-64
ute_ca_apiserver/apps/scheduler/triggers.py                                        33      2    94%   21, 115
ute_ca_apiserver/apps/scheduler/websocket.py                                       69      4    94%   97-98, 162, 200
ute_ca_apiserver/background.py                                                      4      0   100%
ute_ca_apiserver/crud/__init__.py                                                   0      0   100%
ute_ca_apiserver/crud/context.py                                                   11      0   100%
ute_ca_apiserver/crud/dag.py                                                       24     15    38%   24-34, 50, 64-70
ute_ca_apiserver/crud/execution.py                                                 62      2    97%   74, 91
ute_ca_apiserver/crud/file.py                                                      23      0   100%
ute_ca_apiserver/crud/provision.py                                                 28      0   100%
ute_ca_apiserver/crud/task.py                                                      50      4    92%   133, 135, 137-138
ute_ca_apiserver/crud/worker.py                                                    39      3    92%   28-29, 55
ute_ca_apiserver/endpoints/__init__.py                                              0      0   100%
ute_ca_apiserver/endpoints/context.py                                              16      0   100%
ute_ca_apiserver/endpoints/dag.py                                                  24     12    50%   27-31, 48-52, 67-68
ute_ca_apiserver/endpoints/execution.py                                            46      0   100%
ute_ca_apiserver/endpoints/file.py                                                 29      0   100%
ute_ca_apiserver/endpoints/health.py                                                6      0   100%
ute_ca_apiserver/endpoints/provision.py                                            32      1    97%   60
ute_ca_apiserver/endpoints/task.py                                                 27     13    52%   27-32, 49-53, 71-72
ute_ca_apiserver/endpoints/worker.py                                               44      0   100%
ute_ca_apiserver/main.py                                                           35      0   100%
ute_ca_apiserver/models/__init__.py                                                 0      0   100%
ute_ca_apiserver/models/context.py                                                 35      0   100%
ute_ca_apiserver/models/dag.py                                                     37      0   100%
ute_ca_apiserver/models/execution.py                                               43      0   100%
ute_ca_apiserver/models/file.py                                                    15      0   100%
ute_ca_apiserver/models/log.py                                                     14      0   100%
ute_ca_apiserver/models/primitives.py                                               3      0   100%
ute_ca_apiserver/models/provision.py                                               25      0   100%
ute_ca_apiserver/models/task.py                                                    72      0   100%
ute_ca_apiserver/models/variable.py                                                10      0   100%
ute_ca_apiserver/models/worker.py                                                  35      0   100%
ute_ca_apiserver/settings/__init__.py                                               0      0   100%
ute_ca_apiserver/settings/base.py                                                  25      0   100%
ute_ca_apiserver/shared/__init__.py                                                 0      0   100%
ute_ca_apiserver/shared/exceptions.py                                               3      0   100%
ute_ca_apiserver/shared/nested_dict.py                                             18      0   100%
ute_ca_apiserver/shared/websocket.py                                                3      0   100%
ute_ca_apiserver/utils/__init__.py                                                  0      0   100%
ute_ca_apiserver/utils/client.py                                                   64      1    98%   27
ute_ca_apiserver/utils/logger.py                                                   15      7    53%   25-39, 47-51
ute_ca_manager/__init__.py                                                          0      0   100%
ute_ca_manager/apps/__init__.py                                                     0      0   100%
ute_ca_manager/apps/execution_manager/__init__.py                                   0      0   100%
ute_ca_manager/apps/execution_manager/core.py                                      92      8    91%   65-66, 68-69, 93-94, 99, 173
ute_ca_manager/apps/execution_manager/exceptions.py                                 2      0   100%
ute_ca_manager/backend/__init__.py                                                  0      0   100%
ute_ca_manager/backend/provision.py                                               265     35    87%   75-80, 82, 84-87, 94-96, 144, 169, 207, 257, 262, 266, 436-437, 446-474
ute_ca_manager/background.py                                                        2      0   100%
ute_ca_manager/endpoints/__init__.py                                                0      0   100%
ute_ca_manager/endpoints/docs.py                                                    7      1    86%   16
ute_ca_manager/endpoints/health.py                                                  6      0   100%
ute_ca_manager/endpoints/provision.py                                              35      0   100%
ute_ca_manager/exceptions.py                                                        8      0   100%
ute_ca_manager/main.py                                                             19      0   100%
ute_ca_manager/models/__init__.py                                                   0      0   100%
ute_ca_manager/models/provision.py                                                 18      0   100%
ute_ca_manager/utils/__init__.py                                                    0      0   100%
ute_ca_manager/utils/build.py                                                      27      3    89%   55-56, 62
ute_ca_manager/utils/clients/__init__.py                                            0      0   100%
ute_ca_manager/utils/clients/context.py                                            17      0   100%
ute_ca_manager/utils/clients/core.py                                               71      9    87%   136-146
ute_ca_manager/utils/clients/execution.py                                          32      0   100%
ute_ca_manager/utils/clients/file.py                                               14      0   100%
ute_ca_manager/utils/clients/task.py                                               12      1    92%   36
ute_ca_manager/utils/clients/worker.py                                            166      3    98%   51, 269-270
ute_ca_manager/utils/downloader.py                                                 31      0   100%
ute_ca_manager/utils/logger.py                                                     15      0   100%
ute_ca_manager/utils/tl_config/__init__.py                                          0      0   100%
ute_ca_manager/utils/tl_config/base.py                                              8      0   100%
ute_ca_manager/utils/tl_config/credentials.py                                       7      0   100%
ute_ca_manager/utils/tl_config/hw_types.py                                          5      0   100%
ute_ca_manager/utils/tl_config/importer.py                                         18      0   100%
ute_ca_manager/utils/tl_config/parser.py                                           23      0   100%
ute_ca_manager/utils/tl_config/parser_4g.py                                       120      5    96%   94, 106, 131, 197, 203
ute_ca_manager/utils/tl_config/parser_5g.py                                       389     34    91%   155-156, 159, 438, 440, 442-443, 504, 506, 508, 531, 535, 537, 629, 679, 776-779, 885-889, 905-909, 929-930, 977-979
ute_ca_manager/utils/velocity.py                                                   85      5    94%   179-185
ute_ca_worker/__init__.py                                                           0      0   100%
ute_ca_worker/cli.py                                                               12      0   100%
ute_ca_worker/core/__init__.py                                                      0      0   100%
ute_ca_worker/core/args.py                                                         40      1    98%   7
ute_ca_worker/core/command.py                                                      85     11    87%   10, 65, 95, 112, 126-127, 130-133, 148
ute_ca_worker/core/config.py                                                       93      2    98%   91, 103
ute_ca_worker/core/context.py                                                      15      0   100%
ute_ca_worker/core/dag.py                                                          90      6    93%   17, 152, 162, 212-214
ute_ca_worker/core/event.py                                                        43      0   100%
ute_ca_worker/core/executor.py                                                    214     22    90%   106, 117-118, 130, 171, 176-177, 180-200, 271, 277
ute_ca_worker/core/heartbeat.py                                                    18      0   100%
ute_ca_worker/core/lazy_device.py                                                  60      0   100%
ute_ca_worker/core/reactflow.py                                                    26      0   100%
ute_ca_worker/core/router.py                                                       36      0   100%
ute_ca_worker/core/state.py                                                         8      0   100%
ute_ca_worker/core/task.py                                                        240     24    90%   16-17, 92, 264, 282, 293, 299, 580, 717-719, 721-724, 775-777, 779-782, 793, 810
ute_ca_worker/core/variable.py                                                     39      2    95%   85, 97
ute_ca_worker/core/ws.py                                                          125     79    37%   49-51, 55, 59-71, 75, 78-79, 111-112, 119, 122-146, 149-158, 187, 194, 197-220
ute_ca_worker/core/xcom.py                                                         74     10    86%   95-101, 116, 119, 121, 152
ute_ca_worker/dag/__init__.py                                                       0      0   100%
ute_ca_worker/dag/commissioned/__init__.py                                          0      0   100%
ute_ca_worker/dag/commissioned/commissioned/__init__.py                             0      0   100%
ute_ca_worker/dag/commissioned/commissioned/callables.py                           46      0   100%
ute_ca_worker/dag/commissioned/commissioned/dag.py                                 70      0   100%
ute_ca_worker/dag/commissioned/create_stack/__init__.py                             0      0   100%
ute_ca_worker/dag/commissioned/create_stack/callables.py                           46      1    98%   98
ute_ca_worker/dag/commissioned/create_stack/dag.py                                 29      0   100%
ute_ca_worker/dag/commissioned/perform_classical_radio_sw_update/__init__.py        0      0   100%
ute_ca_worker/dag/commissioned/perform_classical_radio_sw_update/callables.py      35      3    91%   83, 95-101
ute_ca_worker/dag/commissioned/perform_classical_radio_sw_update/dag.py            27      0   100%
ute_ca_worker/dag/commissioned/perform_cus_commissioning/__init__.py                0      0   100%
ute_ca_worker/dag/commissioned/perform_cus_commissioning/callables.py              20      0   100%
ute_ca_worker/dag/commissioned/perform_cus_commissioning/dag.py                    15      0   100%
ute_ca_worker/dag/commissioned/perform_ocp_deployment/__init__.py                   0      0   100%
ute_ca_worker/dag/commissioned/perform_ocp_deployment/callables.py                 33      1    97%   95
ute_ca_worker/dag/commissioned/perform_ocp_deployment/commands.py                  43      0   100%
ute_ca_worker/dag/commissioned/perform_ocp_deployment/dag.py                       58      0   100%
ute_ca_worker/dag/commissioned/perform_ocp_vdu_commissioning/__init__.py            0      0   100%
ute_ca_worker/dag/commissioned/perform_ocp_vdu_commissioning/callables.py          61      0   100%
ute_ca_worker/dag/commissioned/perform_ocp_vdu_commissioning/dag.py                21      0   100%
ute_ca_worker/dag/commissioned/perform_sim_commissioning/__init__.py                0      0   100%
ute_ca_worker/dag/commissioned/perform_sim_commissioning/callables.py               9      0   100%
ute_ca_worker/dag/commissioned/perform_sim_commissioning/command.py                71      5    93%   137-141
ute_ca_worker/dag/commissioned/perform_sim_commissioning/dag.py                    38      0   100%
ute_ca_worker/dag/commissioned/perform_sm_commissioning/__init__.py                 0      0   100%
ute_ca_worker/dag/commissioned/perform_sm_commissioning/callables.py               57      0   100%
ute_ca_worker/dag/commissioned/perform_sm_commissioning/dag.py                     53      0   100%
ute_ca_worker/dag/commissioned/perform_vcu_commissioning/__init__.py                0      0   100%
ute_ca_worker/dag/commissioned/perform_vcu_commissioning/callables.py              64      0   100%
ute_ca_worker/dag/commissioned/perform_vcu_commissioning/dag.py                    28      0   100%
ute_ca_worker/dag/commissioned/power_off_device/__init__.py                         0      0   100%
ute_ca_worker/dag/commissioned/power_off_device/dag.py                             17      0   100%
ute_ca_worker/dag/commissioned/reboot_device/__init__.py                            0      0   100%
ute_ca_worker/dag/commissioned/reboot_device/dag.py                                16      0   100%
ute_ca_worker/dag/commissioned/shared/__init__.py                                   0      0   100%
ute_ca_worker/dag/commissioned/shared/callables.py                                 25      0   100%
ute_ca_worker/dag/configured/__init__.py                                            0      0   100%
ute_ca_worker/dag/configured/configured/__init__.py                                 0      0   100%
ute_ca_worker/dag/configured/configured/callables.py                               55      7    87%   45-46, 70-71, 75, 122-123
ute_ca_worker/dag/configured/configured/constants.py                                2      0   100%
ute_ca_worker/dag/configured/configured/dag.py                                     42      0   100%
ute_ca_worker/dag/configured/configured/models.py                                   4      0   100%
ute_ca_worker/dag/configured/reboot_device/__init__.py                              0      0   100%
ute_ca_worker/dag/configured/reboot_device/dag.py                                  12      0   100%
ute_ca_worker/dag/main.py                                                          47      0   100%
ute_ca_worker/dag/on_air/__init__.py                                                0      0   100%
ute_ca_worker/dag/on_air/on_air/__init__.py                                         0      0   100%
ute_ca_worker/dag/on_air/on_air/dag.py                                             17      0   100%
ute_ca_worker/dag/shared/__init__.py                                                0      0   100%
ute_ca_worker/dag/shared/callables.py                                             160     36    78%   228-241, 289-323, 341-342, 346-348, 431-432
ute_ca_worker/dag/shared/execute_hook/__init__.py                                   0      0   100%
ute_ca_worker/dag/shared/execute_hook/commands.py                                  44      0   100%
ute_ca_worker/dag/shared/execute_hook/dag.py                                       25      0   100%
ute_ca_worker/dag/shared/models.py                                                135      1    99%   35
ute_ca_worker/dag/shared/power_off_available_fbbps/__init__.py                      0      0   100%
ute_ca_worker/dag/shared/power_off_available_fbbps/callables.py                    23      1    96%   43
ute_ca_worker/dag/shared/power_off_available_fbbps/dag.py                          12      0   100%
ute_ca_worker/dag/shared/power_on_radios/__init__.py                                0      0   100%
ute_ca_worker/dag/shared/power_on_radios/dag.py                                    13      0   100%
ute_ca_worker/dag/shared/set_up_fbbps/__init__.py                                   0      0   100%
ute_ca_worker/dag/shared/set_up_fbbps/callables.py                                 52      1    98%   65
ute_ca_worker/dag/shared/set_up_fbbps/dag.py                                       14      0   100%
ute_ca_worker/dag/shared/wait_for_states/__init__.py                                0      0   100%
ute_ca_worker/dag/shared/wait_for_states/callables.py                             195      4    98%   46-47, 333-334
ute_ca_worker/dag/shared/wait_for_states/dag.py                                    41      0   100%
ute_ca_worker/dag/shared/wait_for_states/models.py                                 87      0   100%
ute_ca_worker/dag/ssh_only/__init__.py                                              0      0   100%
ute_ca_worker/dag/ssh_only/main.py                                                 10      0   100%
ute_ca_worker/dag/ssh_only/power_on_and_check_ssh_services/__init__.py              0      0   100%
ute_ca_worker/dag/ssh_only/power_on_and_check_ssh_services/callables.py            12      0   100%
ute_ca_worker/dag/ssh_only/power_on_and_check_ssh_services/dag.py                  13      0   100%
ute_ca_worker/dag/ssh_only/shared/__init__.py                                       0      0   100%
ute_ca_worker/dag/ssh_only/shared/callables.py                                     10      0   100%
ute_ca_worker/dag/ssh_only/ssh_only_on_device/__init__.py                           0      0   100%
ute_ca_worker/dag/ssh_only/ssh_only_on_device/callables.py                         10      1    90%   26
ute_ca_worker/dag/ssh_only/ssh_only_on_device/dag.py                               13      0   100%
ute_ca_worker/dag/sw_uploaded/__init__.py                                           0      0   100%
ute_ca_worker/dag/sw_uploaded/ap_sw_update/__init__.py                              0      0   100%
ute_ca_worker/dag/sw_uploaded/ap_sw_update/callables.py                            19      0   100%
ute_ca_worker/dag/sw_uploaded/ap_sw_update/dag.py                                  55      0   100%
ute_ca_worker/dag/sw_uploaded/bts_sw_update/__init__.py                             0      0   100%
ute_ca_worker/dag/sw_uploaded/bts_sw_update/callables.py                           29      2    93%   28, 72
ute_ca_worker/dag/sw_uploaded/bts_sw_update/dag.py                                 63      0   100%
ute_ca_worker/dag/sw_uploaded/callables.py                                         32      0   100%
ute_ca_worker/dag/sw_uploaded/classical_sw_update/__init__.py                       0      0   100%
ute_ca_worker/dag/sw_uploaded/classical_sw_update/callables.py                     70      3    96%   98-100
ute_ca_worker/dag/sw_uploaded/classical_sw_update/commands.py                      70      0   100%
ute_ca_worker/dag/sw_uploaded/classical_sw_update/dag.py                          125      0   100%
ute_ca_worker/dag/sw_uploaded/clean_up_partition/__init__.py                        0      0   100%
ute_ca_worker/dag/sw_uploaded/clean_up_partition/commands.py                       97      0   100%
ute_ca_worker/dag/sw_uploaded/clean_up_partition/dag.py                            16      0   100%
ute_ca_worker/dag/sw_uploaded/cus_sw_update/__init__.py                             0      0   100%
ute_ca_worker/dag/sw_uploaded/cus_sw_update/callables.py                           53      1    98%   53
ute_ca_worker/dag/sw_uploaded/cus_sw_update/commands.py                            34      3    91%   61-65
ute_ca_worker/dag/sw_uploaded/cus_sw_update/constants.py                            1      0   100%
ute_ca_worker/dag/sw_uploaded/cus_sw_update/dag.py                                 29      0   100%
ute_ca_worker/dag/sw_uploaded/cus_sw_update/models.py                              11      0   100%
ute_ca_worker/dag/sw_uploaded/iphy_sw_update/__init__.py                            0      0   100%
ute_ca_worker/dag/sw_uploaded/iphy_sw_update/callables.py                          43      0   100%
ute_ca_worker/dag/sw_uploaded/iphy_sw_update/dag.py                                40      0   100%
ute_ca_worker/dag/sw_uploaded/main.py                                              50      0   100%
ute_ca_worker/dag/sw_uploaded/ocp_sw_update/__init__.py                             0      0   100%
ute_ca_worker/dag/sw_uploaded/ocp_sw_update/callables.py                          123      0   100%
ute_ca_worker/dag/sw_uploaded/ocp_sw_update/dag.py                                 40      0   100%
ute_ca_worker/dag/sw_uploaded/open_stack_sw_update/__init__.py                      0      0   100%
ute_ca_worker/dag/sw_uploaded/open_stack_sw_update/callables.py                    44      2    95%   36, 67
ute_ca_worker/dag/sw_uploaded/open_stack_sw_update/dag.py                          12      0   100%
ute_ca_worker/dag/sw_uploaded/shared/__init__.py                                    0      0   100%
ute_ca_worker/dag/sw_uploaded/shared/callables.py                                 117     16    86%   95, 111, 161-186, 235
ute_ca_worker/dag/sw_uploaded/shared/commands.py                                   16      0   100%
ute_ca_worker/dag/sw_uploaded/shared/constant.py                                   11      0   100%
ute_ca_worker/dag/sw_uploaded/shared/models.py                                     13      0   100%
ute_ca_worker/dag/tools_installation/__init__.py                                    0      0   100%
ute_ca_worker/dag/tools_installation/tools_installation/__init__.py                 0      0   100%
ute_ca_worker/dag/tools_installation/tools_installation/callables.py                5      0   100%
ute_ca_worker/dag/tools_installation/tools_installation/dag.py                     10      0   100%
ute_ca_worker/dag/tools_installation/wts_installation/__init__.py                   0      0   100%
ute_ca_worker/dag/tools_installation/wts_installation/callables.py                 36      0   100%
ute_ca_worker/dag/tools_installation/wts_installation/dag.py                       20      0   100%
ute_ca_worker/exception.py                                                         64      0   100%
ute_ca_worker/lib/__init__.py                                                       0      0   100%
ute_ca_worker/lib/adets.py                                                         51      0   100%
ute_ca_worker/lib/admin.py                                                         15      0   100%
ute_ca_worker/lib/artifactory.py                                                   19      1    95%   38
ute_ca_worker/lib/coam_admin.py                                                    45      1    98%   75
ute_ca_worker/lib/openstack.py                                                     47      0   100%
ute_ca_worker/lib/pdu.py                                                           15      0   100%
ute_ca_worker/lib/ssh.py                                                            7      0   100%
ute_ca_worker/lib/telnet.py                                                       104      8    92%   132, 227, 238-239, 243, 246-248
ute_ca_worker/provision.py                                                         24      0   100%
ute_ca_worker/utils/__init__.py                                                     0      0   100%
ute_ca_worker/utils/client.py                                                     102      0   100%
ute_ca_worker/utils/convert.py                                                      4      0   100%
ute_ca_worker/utils/files.py                                                       18      0   100%
ute_ca_worker/utils/logger.py                                                      18      0   100%
ute_ca_worker/utils/manager.py                                                     25      0   100%
ute_ca_worker/utils/validators.py                                                  64      6    91%   53, 68-72
ute_ca_worker/utils/worker.py                                                      22      2    91%   42, 44
-------------------------------------------------------------------------------------------------------------
TOTAL                                                                           10033    584    94%