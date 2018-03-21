import requests
import json
from requests.auth import HTTPBasicAuth
import logging
from math import floor

init_dashboards = ["_admin","alert","alerts","aws_meltdown_patch_performance_comparisonaverage","aws_patch_comparison","aws_performance_stability_comparison","benchmark__perf-Cloud","benchmark_testing_temp","benchmark_tests_reviewer","bundle_push","case_rule_manage","charting","ci_status","cim_setup","cloud-benchmark__benchmark-dense-searches-200K","cloud-benchmark__benchmark-mixed-searches-200K-i3","cloud-benchmark__benchmark-mixed-searches-200K-i3-4","cloud-benchmark__benchmark-mixed-searches-200K-try","clustering","clustering_v2_5m_for_tameem","core-clustering","core-longevity__longevity_new","core-s2s","core-shc__bpush","core-shc__bpush_smoke","core-shc__regression","core-shc__scheduler","core-shc__shc_regression","core-shc__shc_regression_smoke","dashboards","data_model_editor","data_model_explorer","data_model_manager","data_models","datamodel_audit","dataset","datasets","deploy_server__deploy_server","deploy_server__deploy_server_smoke","deployserver_performance","es-sizing__alerts-capacity-minty-tuned","es_sizing","es_sizing_comparison","es_sizing_legacy","es_sizing_new","es_sizing_tabs","eventtype_tag_center","feature_status","field_extractor","flashtimeline","full_regression","full_regression_result","full_regression_search_result","general_resource_usage_comparison","hec_performance","horizon_chart_gallery","http_new","indexer_clustering","inspection","intel_patch_verification_on_c3","intel_patch_verification_on_c3xlarge__centos_414","job_management","job_manager","kvs_shc__kvs_shc_lookup","kvs_shc__kvs_shc_outputinputlookup","kvs_shc__kvs_shc_primary_failover","kvstore__kvbundlepush","kvstore__kvlookup","kvstore__kvpartialupdate","kvstore__kvsmoke","kvstore__kvupdate","kvstore_bundlepush","kvstore_lookup","kvstore_partialupdate","kvstore_shc_lookup","kvstore_shc_outputinputlookup","kvstore_shc_primary_failover","kvstore_update","longevity_performance","meltdown_patch_indexer_clustering_20180114","mod_setup","nightlight_performance_regression","overview_kpi","overview_pass_rate","overview_statistics","perf_resource_usages","perf_results","performance_smoke_status","performance_smoke_test_triage","performance_status_overview","pivot","predictive_analytics","report","report_builder_define_data","report_builder_display","report_builder_format_report","report_builder_print","reports","resource_usage_comparison","rule_config","s2s_performance","scheduler","search","search__auto_lookup_test","search__batch_mode_search_parallelization_test","search__bucket_count_test","search__bucket_sizes_impact_test","search__bundle_replicate_test","search__dispatch_dir_count_test","search__es_cisco_asa_prebuilt_test","search__es_cisco_asa_test","search__geom_cmd_test","search__locate_data_queries_test","search__lz4_compression_test","search__metadata_elimination_test","search__mini_tsidx_test","search__parallel_reduce_test","search__predicate_pushdown_test","search__prefork_test","search__projection_elimination_cisco_asa_test","search__projection_elimination_win_sec_test","search__sampling_searches_test","search__scheduler_test","search__search_daily_test","search__search_es_test","search__search_filter_test","search__search_result_info_test","search__search_smoke_test","search__smoke_test","search__summarization_dma_data_imbalance_test","search__summarization_dma_es_live_data_test","search__summarization_dma_es_test","search__summarization_dma_ingestion_test","search__summarization_dma_test","search__summarization_ra_test","search__summary_probe_search_test","search__syslog_prebuilt_test","search__tagger_typer_test","search__terms_count_test","search__union_cmd_test","search_auto_lookup","search_batch_mode_search_parallelization","search_bucket_count","search_bucket_count_test","search_bucket_count_test_comparison","search_bucket_sizes_impact","search_bundle_replicate","search_dispatch_dir_count","search_es_cisco_asa","search_es_cisco_asa_prebuilt","search_filter","search_geom_cmd","search_kpi","search_locate_data_queries","search_lz4_compression","search_metadata_elimination","search_mini_tsidx","search_new_batch_mode_search_parallelization","search_new_prefork","search_parallel_reduce","search_predicate_pushdown","search_prefork","search_projection_elimination","search_projection_elimination_cisco_asa","search_projection_elimination_win_sec","search_result_info","search_sampling_searches","search_scheduler","search_small_batch_mode_search_parallelization","search_small_prefork","search_summarization_dma","search_summarization_dma_data_imbalance","search_summarization_dma_es","search_summarization_dma_es_live_data","search_summarization_dma_ingestion","search_summarization_ra","search_summary_probe_search","search_syslog_prebuilt","search_tagger_typer","search_terms_count","search_union_cmd","shc_regression","show_source","splunk_archiver_dashboard","splunk_benchmark","splunk_benchmark_comparison","splunk_cloud_benchmark","splunk_perf_jmeter","splunk_performance_regression__search","splunk_ui_perf","splunk_ui_perf_jmeter","splunk_ui_perf_web_ui","tbd_page","testcase_config","testdata_config","uitest__ui_test_web_restful","uitest__ui_test_web_ui"]
url = "https://ucp-sh01:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/test_jobs"
username="admin"
password="Passw0rd"


def analysis(init_dashboards, dashboards_param_list):
    dashboards = []
    for case_name, feature_name in dashboards_param_list:
        dashboard = {}
        try1 = feature_name+'__'+case_name
        dashboard['dashboard_name'] = try1 if try1 in init_dashboards else feature_name if feature_name in init_dashboards else "null"
        if dashboard['dashboard_name'] == 'null':
            continue
        dashboard['is_primary'] = True
        dashboard['feature_name'] = feature_name
        dashboard['case_name'] = case_name
        dashboards.append(dashboard)
    return dashboards

local_username = 'test'
local_password = 'test'
local_url = 'https://localhost:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/test_dashboards'

def create_collection(collection_name, local_url, local_username, local_password):
    payload = {"name":collection_name}
    response = requests.post(local_url, auth=HTTPBasicAuth(local_username, local_password), verify=0, data=payload)

def insert_dashboards(dashboards, local_url, local_username, local_password):
    header = {'Content-Type': 'application/json'}
    for index, dashboard in enumerate(dashboards):
        dashboard_json = json.dumps(dashboard)
        response = requests.post(local_url, headers=header, auth=HTTPBasicAuth(local_username, local_password), verify=0, data = dashboard_json)
        print("inserting the No.{} item, the result is {}, reason: {}".format(index+1, response.status_code, response.content))
        print(response.text)


batch_url_ucp = "https://ucp-sh01:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/test_dashboards/batch_save"
batch_url = 'https://localhost:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/test_dashboards/batch_save'

def copy_batch(collection_name, local_username, local_password, remote_username, remote_password, remote_url, local_url_batch):
    print("copying from collection {}.".format(collection_name))
    header = {'Content-Type': 'application/json'}
    remote_url = remote_url.format(collection_name)
    response = requests.get(remote_url, auth=HTTPBasicAuth(remote_username, remote_password), verify=0)
    datas = json.loads(response.content.decode("utf-8"))
    full_requests_num = floor(len(datas)/1000)
    for i in range(full_requests_num):
        datas_json = json.dumps(datas[i*1000:(i*1000+1000)]) 
        response = requests.post(local_url_batch.format(collection_name), data=datas_json, auth=HTTPBasicAuth(local_username, local_password), verify=0, headers=header)
    # fetch the reamain datas
    datas_json = json.dumps(datas[full_requests_num*1000:]) 
    response = requests.post(local_url_batch.format(collection_name), data=datas_json, auth=HTTPBasicAuth(local_username, local_password), verify=0, headers=header)
    print("insert result:{}.".format(response.text))


def insert_batch(dashboards, batch_url, local_username, local_password):
    header = {'Content-Type': 'application/json'}
    dashboards_json = json.dumps(dashboards)
    response = requests.post(batch_url, headers=header, data = dashboards_json, auth=HTTPBasicAuth(local_username, local_password), verify=0)
    print("insert result:{}. numbers:{}".format(response.text, len(response.text)))
# insert_batch(dashboards,batch_url, local_username, local_password)

def clear_local(collections, base_url, local_username, local_password):
    if type(collections) != type([]):
        collections = [collections]
    for collection in collections:
        print("cleaning data from collection: {}".format(collection))
        url = base_url.format(collection)
        response = requests.delete(url, auth=HTTPBasicAuth(local_username, local_password), verify=0)




if __name__ == '__main__':
   # clear local kv datas
    local_base_url = 'https://localhost:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/{}'
    # collections = ['rules', 'test_case_with_rules', 'test_case_result_jobs', 'test_case_results',
    # 'test_meta_job_name_lookup', 'test_case_kpis', 'baseline', 'test_jobs', 'test_dashboards']
    collections = ['test_dashboards']
    clear_local(collections, local_base_url, local_username, local_password)

    # map case_name to dashboard_name
    # response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=0)
    # test_jobs=json.loads(response.content.decode("utf-8"))
    # dashboards_param_list = [ (testjob["testJobSummary"]["case_name"], testjob["testJobSummary"]["feature_name"]) for testjob in test_jobs if "testJobSummary" in testjob]
    # print(len(dashboards_param_list))
    # dashboards_param_list = list(set(dashboards_param_list))
    # print(len(dashboards_param_list))
    # dashboards = analysis(init_dashboards, dashboards_param_list)
    # print("dashboards: {}, param_list: {}".format(len(dashboards), len(dashboards_param_list)))
    # insert_batch(dashboards, batch_url_ucp, username, password)

    # copy kv data from ucp
    # collections = ['rules', 'test_case_with_rules', 'test_case_result_jobs', 'test_case_results',
    # 'test_meta_job_name_lookup', 'test_case_kpis', 'baseline', 'test_jobs']
    remote_url = "https://ucp-sh01:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/{}"
    local_url = 'https://localhost:8089/servicesNS/nobody/splunk_app_perf_automation/storage/collections/data/{}/batch_save'
    for collection in collections:
        copy_batch(collection, local_username, local_password, username, password, remote_url, local_url)

 
    

        
        
