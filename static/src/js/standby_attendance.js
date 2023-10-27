odoo.define('hr_standby.my_attendances', function (require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');
var field_utils = require('web.field_utils');
var MyAttendances = require('hr_time_tracking.my_attendances')

const session = require('web.session');

MyAttendances.include({

    events: {
        "click .o_hr_home_office": _.debounce(function() {
            this.update_attendance_homeoffice();
        }, 200, true),
        "click .o_hr_attendance_sign_in_out_icon": _.debounce(function() {
            this.update_attendance();
        }, 200, true),
        "click .o_hr_standby": _.debounce(function() {
            this.create_attendance_standby();
        }, 200, true),
        "click .hr_standby": _.debounce(function() {
            this.close_attendance_standby();
        }, 200, true),

    },


    update_attendance: function () {
          var self = this;
     this._super();;
    },

    update_attendance_homeoffice: function () {
     var self = this;
     this._super();
    },

    create_attendance_standby: function () {
    var self = this;
    this._rpc({
            model: 'hr.standby',
            method: 'create_hr_standby',
            args: [[self.employee.id],'hr_attendance.hr_attendance_action_my_attendances'],
            context: session.user_context,
        })
        .then(function(result) {
            if (result.action) {
                 self.do_action(result.action);
            } else if (result.warning) {
                self.displayNotification({ title: result.warning, type: 'danger' });
            }
        });

    },

  close_attendance_standby: function () {
    var self = this;
    this._rpc({
            model: 'hr.standby',
            method: 'close_hr_standby',
            args: [[self.employee.id]],
            context: session.user_context,
        })

    },
    });

});
