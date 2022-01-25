"""
method 2 to call flask_samestatic
"""
from flask import Flask, Blueprint
from samstatic_flask import FlaskWithSamStatic
from samstatic_flask import SamStatic

if __name__ == '__main__':
    app = FlaskWithSamStatic(__name__)
    # app.config['SAMSTATIC_ENDPOINTS'] = SamStatic.options.ALL  # default. {'static', 'subapp_shadow.static', 'subapp.static'}
    # app.config['SAMSTATIC_ENDPOINTS'] = SamStatic.options.DEACTIVE  # deactivate samestatic_flask
    # app.config['SAMSTATIC_ENDPOINTS'] = (SamStatic.options.ALLOWED, {'subapp_shadow.static'}) # {'subapp_shadow.static'}
    # app.config['SAMSTATIC_ENDPOINTS'] = (SamStatic.options.DISALLOWED, {'subapp_shadow.static'}) # {'static', 'subapp.static'}

    app.register_blueprint(Blueprint('subapp_shadow', __name__,
                                     static_url_path='/static',
                                     static_folder='static_subapp_upload'))
    app.register_blueprint(Blueprint('subapp', __name__,
                                     static_url_path='/static',
                                     static_folder='static_subapp_default'))

    app.run(debug=True)

    # default option:
    # http://127.0.0.1:5000/static/myname.html  ->  static_subapp_upload/myname.html
    # http://127.0.0.1:5000/static/myemail.html  ->  static_subapp_upload/myemail.html
    # http://127.0.0.1:5000/static/mysex.html  ->  static_subapp_default/mysex.html
