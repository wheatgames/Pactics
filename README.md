# Pactics 玩家资料网站

隐私政策、用户协议、账号删除说明和玩家支持的独立网站。正文使用 Markdown，共用自有页面模板和样式，由 GitHub Pages 生成并托管。

## 日常修改

直接编辑根目录的四份文档：

| 文件 | 页面 |
| --- | --- |
| privacy.md | 隐私政策 |
| terms.md | 用户协议 |
| delete-account.md | 账号删除说明 |
| support.md | 支持与常见问题 |

四份文档是本站的发布正文。首页和目录会从共用配置及文档标题生成，无需再维护一份重复的隐私政策。

- 页面入口和简介在 `_data/navigation.yml`。
- 联系邮箱、域名和仓库路径在 `_config.yml`。
- 页面结构在 `_layouts/`，样式在 `assets/site.css`。
- 网站没有前端 JavaScript、统计、Cookie 或第三方字体请求；系统字体直接显示正文。

## 发布到 GitHub Pages

在 GitHub 仓库 **Settings → Pages** 中，选择 **Deploy from a branch**，分支选 **main**，目录选 **/(root)**，保存。

推送修改后，GitHub 会构建并更新网站。到仓库 **Actions** 查看构建结果，构建成功后访问：

- 首页：https://wheatgames.github.io/Pactics/
- 隐私政策：https://wheatgames.github.io/Pactics/privacy.html
- 用户协议：https://wheatgames.github.io/Pactics/terms.html
- 账号删除：https://wheatgames.github.io/Pactics/delete-account.html
- 支持：https://wheatgames.github.io/Pactics/support.html

项目已配置 `url: https://wheatgames.github.io` 和 `baseurl: /Pactics`。所有站内链接和资源地址都通过 Jekyll 生成，避免错误加载账号主页的样式。

如果未来复制给另一个 App，需要更改 `_config.yml` 的域名、仓库路径和邮箱，再修改文档、导航和品牌。使用独立域名时，按实际托管位置调整 `url`、`baseurl` 和 GitHub Pages 的域名设置。

## 本地预览（可选）

仅在线改字并发布时，无需安装本地开发工具。要在电脑上预览，安装 Ruby 和 Bundler，然后在仓库目录执行：

```text
bundle install
bundle exec jekyll serve
```

打开终端显示的地址，通常是 http://127.0.0.1:4000/Pactics/ 。本地依赖使用 Jekyll 及其 Markdown 解析器，没有额外的主题或前端打包工具。依赖锁文件由 Bundler 根据当前系统生成，不随仓库提交。

## 发布前检查（可选）

安装 Python 3 后，可以检查生成页面的站内链接、目录锚点和样式文件：

```text
bundle exec jekyll build
python scripts/check_site.py _site --baseurl /Pactics
```

检查不访问外部服务，也不修改协议正文。手机布局、目录展开和邮件链接应同时用浏览器确认。
