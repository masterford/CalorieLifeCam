# -*- coding: utf-8 -*- #
# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Delete autoscaling policy command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dataproc import dataproc as dp
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dataproc import flags
from googlecloudsdk.core.console import console_io


class Delete(base.DeleteCommand):
  """Delete an autoscaling policy."""

  @staticmethod
  def Args(parser):
    flags.AddAutoscalingPolicyResourceArg(
        parser, 'delete', api_version='v1beta2')

  def Run(self, args):
    dataproc = dp.Dataproc(self.ReleaseTrack())
    messages = dataproc.messages

    policy_ref = args.CONCEPTS.autoscaling_policy.Parse()

    request = messages.DataprocProjectsRegionsAutoscalingPoliciesDeleteRequest(
        name=policy_ref.RelativeName())

    console_io.PromptContinue(
        message="The autoscaling policy '[{0}]' will be deleted.".format(
            policy_ref.Name()),
        cancel_on_no=True)

    dataproc.client.projects_regions_autoscalingPolicies.Delete(request)
