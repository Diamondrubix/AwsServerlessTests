exports.handler = (event, context, callback) => {


    var SSH = require('simple-ssh');
    var ssh = new SSH({
        host: event,//'ec2-54-91-69-153.compute-1.amazonaws.com'
        user: 'aarato',
        pass: 'Password123'
    });
//'echo $PATH'
//sudo ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key

    ssh.exec('ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key.pub', {
        pty: true,
        out: function(stdout) {
            //console.log(stdout);
            callback(null, String(stdout))
        }
    }).start();

    callback(null,"this was a failure");
};
