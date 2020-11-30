#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bqpipeline.bqpipeline import BQPipeline
import sys

if __name__ == "__main__":
    JOB_NAME = sys.argv[1]
    PROJECT = sys.argv[2]
    DATASET = sys.argv[3]
    DEST_DATASET = sys.argv[4]
    bq = BQPipeline(job_name=JOB_NAME,
                    query_project=PROJECT,
                    default_project=PROJECT,
                    default_dataset=DATASET,
                    json_credentials_path='credentials.json')

    replacements = {
        'project': PROJECT,
        'dataset': DATASET,
        'dataset_dest': DEST_DATASET
    }

    # It's possible to leave project and dataset unspecified if defaults have been set
    order_details = '.'.join([PROJECT, DEST_DATASET, 'order_details']) 
    orders_list = '.'.join([DEST_DATASET, 'orders_list'])
    orders_merged = '.'.join([PROJECT, DEST_DATASET, 'orders_merged'])
    state_performance = '.'.join([PROJECT,DEST_DATASET,'state_performance'])
    city_performance = '.'.join([DEST_DATASET,'city_performance'])
    sales_target = '.'.join([DEST_DATASET,'sales_target'])
    category_items_sold = ''.join([DEST_DATASET,'category_items_sold'])
    sales_target_comparison = '.'.join([DEST_DATASET,'sales_target_comparison'])
    sub_category_items_sold = '.'.join([DEST_DATASET,'sub_category_items_sold'])
    tbl4 = '.'.join([PROJECT, DATASET, 'tmp_table_4'])

    bq.run_queries( 
        [
            ('order_details.sql', order_details),
            ('orders_list.sql', orders_list),
            ('orders_merged.sql', orders_merged),
            ('state_performance.sql', state_performance),
            ('sales_target.sql',sales_target),
            ('city_performance.sql', city_performance),
            ('category_items_sold.sql',category_items_sold),
            ('sales_target_comparison.sql',sales_target_comparison),
            ('sub_category_items_sold.sql',sub_category_items_sold)

        ],
        **replacements
    )

    bq.copy_table(state_performance, tbl4)
    
