from django.conf import settings


def script(form, validatejs):

  fields = []

  for field in form.fields:

    fields.append(" { name: '" + field + "', rules: 'required', 'id': 'id_" + form[field].label + "' } ")

    # display: 'required', \
    # display: 'min length', \
    # display: 'password confirmation', \
    # rules: 'required|matches[password]' \
    # rules: 'valid_email' \
    # rules: 'min_length[8]' \
    # rules: 'alpha_numeric' \
    # rules: 'required' \

  validatejs['script'] = ''

  if 'steal_js' in settings.VALIDATEJS and settings.VALIDATEJS['steal_js']:
    validatejs['script'] += '<script type="text/javascript" src="http://rickharrison.github.com/validate.js/validate.min.js"></script>'

  validatejs['script'] += '<script type="text/javascript">'
  validatejs['script'] += "var validator = new FormValidator('" + validatejs['form_name'] + "', [ "

  validatejs['script'] += ','.join(map(str, fields))
                            
  validatejs['script'] += " ], function(errors, events) { if (errors.length > 0) { "

  for field in form.fields:

    validatejs['script'] += '$("#id_' + form[field].label.lower() + '").parent().addClass("error");'

  validatejs['script'] += " } } ); </script> "

  if 'default_css' in settings.VALIDATEJS and settings.VALIDATEJS['default_css']:
    validatejs['script'] += '<style type="text/css">.error { border: red 2px dashed; } </style>'

  return validatejs
