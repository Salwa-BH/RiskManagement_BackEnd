/* # Manually add values to websitestructure table in PgAdmin4 */

INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Dashboard', 'Dashboard');

INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Process', 'Map');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Process', 'SIPOC');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Process', 'DICTIONARY');


INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Map');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Identification');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Characterisation');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Assessment');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Risk Control');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Incident');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Action plan');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Risk', 'Dictionary');

INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Settings', 'Settings');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Settings', 'Administration settings');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Settings', 'Company sites');
INSERT INTO public.permissions_websitestructure( structure, sub_structure ) VALUES ( 'Settings', 'Permissions');

/* # Company's site*/
INSERT INTO public.processes_companysite( name, is_default) VALUES ('Casablanca', true);
INSERT INTO public.processes_companysite( name, is_default) VALUES ('Tanger', false);

/* # Profile, */
INSERT INTO public.permissions_profile(name) VALUES ('RH');
INSERT INTO public.permissions_profile(name) VALUES ('Direction');
/* # Group */
INSERT INTO public.permissions_group(name) VALUES ('Group 1');
INSERT INTO public.permissions_group(name) VALUES ('Group 2');
/* # ROLE*/
INSERT INTO public.permissions_role( name, depth, numchild, path, confirmation) VALUES ( 'CEO', 1, 1, '0001', false);
INSERT INTO public.permissions_role( name, depth, numchild, path, confirmation) VALUES ( 'Senior Manager', 2, 1, '00010001', false);
INSERT INTO public.permissions_role( name, depth, numchild, path, confirmation) VALUES ( 'Junior Manager', 3, 0, '000100010001', true);
/* # Permissions*/
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,1);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,2);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,3);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,4);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,5);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,6);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,7);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,8);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,9);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,10);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,11);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,12);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,13);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,14);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,1,15);

INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,1);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,2);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,3);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,4);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,5);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,6);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,7);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,8);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,9);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,10);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,11);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,12);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,13);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,14);
INSERT INTO public.permissions_permissions( read, "create", edit, erase, profile_id_id, structure_id_id) VALUES (true,true,true,true,2,15);

/* ################################################### PROCESS     ################################################### */

/* # PROCESS TYPES*/
INSERT INTO public.processes_processtype(path, depth, numchild, name, is_default) VALUES ( '0001', 1, 1, 'Domain', true);
INSERT INTO public.processes_processtype(path, depth, numchild, name, is_default) VALUES ( '00010001', 2, 1, 'Process', false);
INSERT INTO public.processes_processtype(path, depth, numchild, name, is_default) VALUES ( '000100010001', 3, 1, 'Activity', false);
INSERT INTO public.processes_processtype(path, depth, numchild, name, is_default) VALUES ( '0001000100010001', 4, 1, 'Sub_Activity', false);

/* # Players*/
INSERT INTO public.processes_player(short_name, long_name, depth, nature, numchild, path, start_date) VALUES ( 'short_name1', 'name1', 1, 'function', 0, '0001', '2021-09-20');
INSERT INTO public.processes_player(short_name, long_name, depth, nature, numchild, path, start_date) VALUES ( 'short_name2', 'name2', 1, 'function', 0, '0002', '2021-09-20');

/* # I/Os*/
INSERT INTO public.processes_ioelement( name ) VALUES ('I/O 1');
INSERT INTO public.processes_ioelement( name ) VALUES ('I/O 2');

/* # Process Status*/
INSERT INTO public.processes_statusprocess(name) VALUES ('Empty');
INSERT INTO public.processes_statusprocess(name) VALUES ('In progress');
INSERT INTO public.processes_statusprocess(name) VALUES ('Complete');
 
/* # PROCESS*/
INSERT INTO public.processes_process(path, depth, numchild, title, company_site_id, process_type_id, status, start_date) VALUES ('0001' ,1,1,'Domain1',1,1, 'In progress', '2021-09-20');
INSERT INTO public.processes_process(path, depth, numchild, title, company_site_id, process_type_id, status, start_date) VALUES ('00010001' ,2,1,'Process1',1,1, 'In progress', '2021-09-20');
INSERT INTO public.processes_process(path, depth, numchild, title, company_site_id, process_type_id, status, start_date) VALUES ('000100010001' ,3,1,'Activity1',1,1, 'Complete', '2021-09-20');
INSERT INTO public.processes_process(path, depth, numchild, title, company_site_id, process_type_id, status, start_date) VALUES ('0001000100010001' ,4,0,'Sub_Activity_1',1,1, 'Empty', '2021-09-20');

/* ###################################################   RISK     ################################################### */

/* # basel_event*/
INSERT INTO public.risks_basel(name) VALUES ('base_event_1');
INSERT INTO public.risks_basel(name) VALUES ('base_event_2');
INSERT INTO public.risks_basel(name) VALUES ('base_event_3');

/* # Factors*/
INSERT INTO public.risks_factor( category, name) VALUES ('Factor_1', 'Internal');
INSERT INTO public.risks_factor( category, name) VALUES ('Factor_2', 'External');

/* # Impacts */
INSERT INTO public.risks_impact(name) VALUES ('Low');
INSERT INTO public.risks_impact(name) VALUES ('High');
INSERT INTO public.risks_impact(name) VALUES ('Major');
INSERT INTO public.risks_impact(name) VALUES ('Extreme');

/* # Products*/
INSERT INTO public.risks_product(category, name) VALUES ('Product', 'Product_1');
INSERT INTO public.risks_product(category, name) VALUES ('Product', 'Product_2');
INSERT INTO public.risks_product(category, name) VALUES ('Service', 'Service_1');
INSERT INTO public.risks_product(category, name) VALUES ('Service', 'Service_2');

/* # Frequency */
INSERT INTO public.risks_frequencyrisk(name) VALUES ('Very rare');
INSERT INTO public.risks_frequencyrisk(name) VALUES ('Rare');
INSERT INTO public.risks_frequencyrisk(name) VALUES ('Normal');
INSERT INTO public.risks_frequencyrisk(name) VALUES ('Frequent');
INSERT INTO public.risks_frequencyrisk(name) VALUES ('Vere frequent');

/* # Criticality*/
INSERT INTO public.risks_criticality_risk(name) VALUES ('Criticality_1');
INSERT INTO public.risks_criticality_risk(name) VALUES ('Criticality_2');
INSERT INTO public.risks_criticality_risk(name) VALUES ('Criticality_3');

/* # Incident Priority*/
INSERT INTO public.risks_priorityincident(name) VALUES ('Priority_1');
INSERT INTO public.risks_priorityincident(name) VALUES ('Priority_2');
INSERT INTO public.risks_priorityincident(name) VALUES ('Priority_3');

/* # Criticality Incident*/
INSERT INTO public.risks_criticalityincident(name) VALUES ('Criticality_Incident_1');
INSERT INTO public.risks_criticalityincident(name) VALUES ('Criticality_Incident_2');
INSERT INTO public.risks_criticalityincident(name) VALUES ('Criticality_Incident_3');

/* # Action Plan Status*/
INSERT INTO public.risks_statusap(name) VALUES ('Status_1');
INSERT INTO public.risks_statusap(name) VALUES ('Status_2');
INSERT INTO public.risks_statusap(name) VALUES ('Status_3');

/* # Action Plan Category*/
INSERT INTO public.risks_categoryap(name) VALUES ('ap_category_1');
INSERT INTO public.risks_categoryap(name) VALUES ('ap_category_2');
INSERT INTO public.risks_categoryap(name) VALUES ('ap_category_3');

/* # Action plan Effort */
INSERT INTO public.risks_effortap(name) VALUES ('effort_1');
INSERT INTO public.risks_effortap(name) VALUES ('effort_2');
INSERT INTO public.risks_effortap(name) VALUES ('effort_3');


