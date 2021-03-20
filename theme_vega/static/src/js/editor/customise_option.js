//--------------------------------------------------------------------------
//Customise Option file included
//--------------------------------------------------------------------------
harpiya.define('theme_vega.options', function (require) {
'use strict';

var core = require('web.core');
var QWeb = core.qweb;

QWeb.add_template('/theme_vega/static/src/xml/customise_option.xml');

})
