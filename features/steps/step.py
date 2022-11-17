from behave import *
from functions.functions import myFunctions

use_step_matcher("re")


@given("test skeleton class")
def step_impl(context):
    myFunctions.suma(context)

@then("sum (\d+) to the result")
def step_impl(context, num):
    myFunctions.sum_to_result(context, num)

