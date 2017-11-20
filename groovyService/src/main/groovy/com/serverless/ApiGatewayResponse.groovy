package com.serverless

import groovy.transform.CompileStatic
import groovy.transform.builder.Builder

/**
 * @author Laurent Krishnathas
 * @version 2017
 */

@Builder
@CompileStatic
class ApiGatewayResponse {
  int statusCode
  String body
  Map<String, String> headers
}
