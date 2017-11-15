package com.serverless

import groovy.json.JsonOutput
import groovy.transform.CompileStatic
import groovy.transform.builder.Builder

/**
 * @author Laurent Krishnathas
 * @version 2017
 */
@Builder
@CompileStatic
class Response {
  Object message
  Map<String, Object> input

  String toJson() {
    return JsonOutput.prettyPrint(JsonOutput.toJson(this))
  }
}
