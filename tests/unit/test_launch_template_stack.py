import aws_cdk as core
import aws_cdk.assertions as assertions

from launch_template.launch_template_stack import LaunchTemplateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in launch_template/launch_template_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LaunchTemplateStack(app, "launch-template")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
