const checkInitField = async (csrfToken) => {
    const fields = [
        {id: 'blog_user', tipId: 'blog_user_tip', message: '账号不能为空！'},
        {id: 'blog_full_name', tipId: 'blog_full_name_tip', message: '用户名不能为空！'},
        {id: 'blog_email', tipId: 'blog_email_tip', message: '邮箱不能为空！'},
        {id: 'blog_password1', tipId: 'blog_password1_tip', message: '密码不能为空！'},
        {id: 'blog_password2', tipId: 'blog_password2_tip', message: '密码不能为空！'},
        {id: 'blog_domain', tipId: 'blog_domain_tip', message: '博客链接不能为空！'},
        {id: 'blog_title', tipId: 'blog_title_tip', message: '博客标题不能为空！'}
    ];

    let flag = true;

    fields.forEach(field => {
        const element = document.getElementById(field.id);
        const tipElement = document.getElementById(field.tipId);

        if (element.value === '') {
            tipElement.textContent = '* ' + field.message;
            flag = false;
        }
    });

    const blog_password1 = document.getElementById('blog_password1').value;
    const blog_password2 = document.getElementById('blog_password2').value;

    if (blog_password1 !== blog_password2) {
        document.getElementById('blog_password2_tip').textContent = '* 密码两次输入不一致！';
        flag = false;
    }

    if (flag) {
        try {
            const data = {
                blog_user: blog_user.value,
                blog_full_name: blog_full_name.value,
                blog_email: blog_email.value,
                blog_password: blog_password1,
                blog_domain: blog_domain.value,
                blog_title: blog_title.value,
            };

            const response = await fetch(window.location.href, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(data)
            });

            console.log(window.location.href)

            const responseData = await response.json();

            if (responseData.status === 200) {
                window.location.href = '/';
            } else {
                console.log('请检查数据库连接、网络连接、以及端口可访问性！');
            }
        } catch (error) {
            console.error('发生错误:', error);
        }
    }
};

const clearId = (Id) => {
    document.getElementById(Id).textContent = ''
}

const clearInput = (Id) => {
    document.getElementById(Id).value = ''
}