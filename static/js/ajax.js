$(function() {

    $('#sign-up').validate({
        rules:
        {
            name: {
                required: true,
                minlength: 2,
                maxlength: 20
            },
            lastname: {
                required: true,
                minlength: 2
            },
            uname: {
                required: true,
                minlength: 4
            },
            pwd: {
                required: true,
                minlength: 6,
                maxlength: 20
            },
            pwd_again: {
                required: true,
                equalTo: '#pwd'
            },
            email: {
                required: true,
                email: true
            },
        },
        messages:
        {
            name: "Enter a valid name",
            lastname: "Enter a valid lastname",
            uname: "Enter a valid username",
            pwd:{
                required: "Provide a password",
                minlength: "Password needs to be minimum of 6 characters"
            },
            email: "Enter a valid email",
            pwd_again:{
                required: "Retype your password",
                equalTo: "Password mismatch! Retype"
            }
        },
        submitHandler: $(this).submit()
    });

    $.validator.setDefaults({
        highlight: function(element) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).closest('.form-group').removeClass('has-error');
        },
        errorElement: 'span',
        errorClass: 'help-block',
        errorPlacement: function(error, element) {
            if(element.parent('.form-group').length) {
                error.insertAfter(element.parent());
            } else {
                error.insertAfter(element);
            }
        }
    });

    $("#sign-up, #sign-in").submit(function(e) {
        e.preventDefault();

        var data = $(this).serialize();
        var uri = $(this).attr('action');
        var met = $(this).attr('method');
        
        $.ajax({
            beforeSend: $(this).valid(),
            url: uri,
            type: met,
            dataType: 'json',
            data: data,
        })
        .done(function() {
            console.log("success");
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
            console.log("complete");
        });
    });
    $('#sign-up #uname').focusout(function(e) {
        
    });
});