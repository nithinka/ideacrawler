#/*************************************************************************
# *
# * Copyright 2018 Ideas2IT Technology Services Private Limited.
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *     http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *
# ***********************************************************************/

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ideacrawler_pb2 as ideacrawler__pb2


class IdeaCrawlerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddDomainAndListen = channel.unary_stream(
        '/protofiles.IdeaCrawler/AddDomainAndListen',
        request_serializer=ideacrawler__pb2.DomainOpt.SerializeToString,
        response_deserializer=ideacrawler__pb2.PageHTML.FromString,
        )
    self.AddPages = channel.stream_unary(
        '/protofiles.IdeaCrawler/AddPages',
        request_serializer=ideacrawler__pb2.PageRequest.SerializeToString,
        response_deserializer=ideacrawler__pb2.Status.FromString,
        )
    self.CancelJob = channel.unary_unary(
        '/protofiles.IdeaCrawler/CancelJob',
        request_serializer=ideacrawler__pb2.Subscription.SerializeToString,
        response_deserializer=ideacrawler__pb2.Status.FromString,
        )


class IdeaCrawlerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddDomainAndListen(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPages(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IdeaCrawlerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddDomainAndListen': grpc.unary_stream_rpc_method_handler(
          servicer.AddDomainAndListen,
          request_deserializer=ideacrawler__pb2.DomainOpt.FromString,
          response_serializer=ideacrawler__pb2.PageHTML.SerializeToString,
      ),
      'AddPages': grpc.stream_unary_rpc_method_handler(
          servicer.AddPages,
          request_deserializer=ideacrawler__pb2.PageRequest.FromString,
          response_serializer=ideacrawler__pb2.Status.SerializeToString,
      ),
      'CancelJob': grpc.unary_unary_rpc_method_handler(
          servicer.CancelJob,
          request_deserializer=ideacrawler__pb2.Subscription.FromString,
          response_serializer=ideacrawler__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protofiles.IdeaCrawler', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
