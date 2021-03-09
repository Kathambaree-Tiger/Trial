# Databricks notebook source
# Connect to the Java logger 
log4jref = sc._jvm.org.apache.log4j
LOGGER = log4jref.LogManager.getLogger('aiAppender')
LOGGER.info("INFO: Hi from App Insights on Databricks")
LOGGER.warn("WARN: Hi from App Insights on Databricks")

# COMMAND ----------

import os
# This package must be installed on the Databricks Cluster from Pypi
from applicationinsights import TelemetryClient

tc = TelemetryClient(os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY"))

# COMMAND ----------

tc.track_event('Python Custom Event Fired')
tc.flush()

# COMMAND ----------

