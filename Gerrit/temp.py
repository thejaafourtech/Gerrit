
iileName = sdk_classes_path+file_name+'.py'
template = jinja2_env.get_template('sdkTemplateMain.txt')
sdk_gen_name = os.path.basename(fileName).split('.')[-2]
with open(sdk_classes_path+file_name+'Main.py', mode='w') as sdk:
    sdk.write(template.render({"sdk_gen_name": sdk_gen_name,
                               "class_name": class_name,
                               'func_arguments': ordered_func_arguments}))
