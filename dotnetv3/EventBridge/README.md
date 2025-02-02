<!--Generated by WRITEME on 2023-03-07 15:33:01.600488 (UTC)-->
# EventBridge code examples for the SDK for .NET

## Overview

Shows how to use the AWS SDK for .NET to work with Amazon EventBridge.

<!--custom.overview.start-->
<!--custom.overview.end-->

*EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources.*

## ⚠ Important

* Running this code might result in charges to your AWS account.
* Running the tests might result in charges to your AWS account.
* We recommend that you grant your code least privilege. At most, grant only the minimum permissions required to perform the task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
* This code is not tested in every AWS Region. For more information, see [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services).

<!--custom.important.start-->
<!--custom.important.end-->

## Code examples

### Get started

* [Hello EventBridge](Actions/HelloEventBridge.cs#L4) (`ListEventBuses`)

### Single actions

Code excerpts that show you how to call individual service functions.

* [Add a target](Actions/EventBridgeWrapper.cs#L349) (`PutTargets`)
* [Create a rule](Actions/EventBridgeWrapper.cs#L168) (`PutRule`)
* [Delete a rule](Actions/EventBridgeWrapper.cs#L435) (`DeleteRule`)
* [Describe a rule](Actions/EventBridgeWrapper.cs#L35) (`DescribeRule`)
* [Disable a rule](Actions/EventBridgeWrapper.cs#L71) (`DisableRule`)
* [Enable a rule](Actions/EventBridgeWrapper.cs#L54) (`EnableRule`)
* [List rule names for a target](Actions/EventBridgeWrapper.cs#L142) (`ListRuleNamesByTarget`)
* [List rules](Actions/EventBridgeWrapper.cs#L89) (`ListRules`)
* [List targets for a rule](Actions/EventBridgeWrapper.cs#L116) (`ListTargetsByRule`)
* [Remove targets from a rule](Actions/EventBridgeWrapper.cs#L393) (`RemoveTargets`)
* [Send events](Actions/EventBridgeWrapper.cs#L292) (`PutEvents`)

### Scenarios

Code examples that show you how to accomplish a specific task by calling multiple
functions within the same service.

* [Get started with rules and targets](Scenarios/EventBridgeScenario.cs) 

## Run the examples

### Prerequisites

For prerequisites, see the [README](../README.md#Prerequisites) in the `dotnetv3` folder.

<!--custom.prerequisites.start-->
<!--custom.prerequisites.end-->

### Instructions

<!--custom.instructions.start-->
Before you compile the .NET application, you can optionally set configuration values
in the settings.json file. These settings include topic and bucket name settings for
working with rules and targets. Alternatively, add a settings.local.json file with
your local settings, which will be loaded automatically when the application runs.

After the example compiles, you can run it from the command line. To do so, navigate to
the folder that contains the .csproj file and run the following command:

```
dotnet run
```
Alternatively, you can run the example from within your IDE.
<!--custom.instructions.end-->

#### Hello EventBridge

This example shows you how to get started using EventBridge.


#### Get started with rules and targets

This example shows you how to do the following:

* Create a rule.
* Add a target to a rule.
* Enable and disable rules.
* List rules and targets.
* Update rules and targets.
* Send events.
* Delete the rule.

<!--custom.scenarios.eventbridge_Scenario_GettingStarted.start-->
<!--custom.scenarios.eventbridge_Scenario_GettingStarted.end-->

### Tests

⚠ Running tests might result in charges to your AWS account.

To find instructions for running these tests, see the [README](../README.md#Tests)
in the `dotnetv3` folder.

<!--custom.tests.start-->
<!--custom.tests.end-->

## Additional resources

* [EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
* [EventBridge API Reference](https://docs.aws.amazon.com/eventbridge/latest/APIReference/Welcome.html)
* [SDK for .NET EventBridge reference](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/EventBridge/NEventBridge.html)

<!--custom.resources.start-->
<!--custom.resources.end-->

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0