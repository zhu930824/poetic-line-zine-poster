# Poetic Line Zine Poster

一个用于 Codex 的图像生成 Skill：把用户照片保留为忠实摄影区域，并在下方加入由原图关系提炼出的抽象记忆面板。

抽象面板默认采用：

- 宽炭笔 / 石墨侧锋扫线
- 一条连续的彩色涂鸦线
- 小尺度实验性 zine 排版
- 干净、无纹理的象牙色背景

## 安装

将仓库克隆到 Codex Skills 目录：

```powershell
git clone https://github.com/zhu930824/poetic-line-zine-poster.git "$env:USERPROFILE\.codex\skills\poetic-line-zine-poster"
```

重新打开 Codex 后，即可通过 `$poetic-line-zine-poster` 调用。

## 使用

上传一张照片，然后输入：

```text
使用 $poetic-line-zine-poster 处理这张照片。
```

指定严格的 9:16 输出：

```text
使用 $poetic-line-zine-poster 处理这张照片。输出 9:16。
```

也可以补充唯一的照片外强调色，例如：

```text
使用 $poetic-line-zine-poster 处理这张照片，用几笔钴蓝色线条点缀。
```

## 设计原则

Skill 遵循以下流程：

```text
DECONSTRUCT → SELECTIVE PRESERVATION → ABSTRACT / DISTILL → RECONSTRUCT
```

核心要求包括：

- 摄影区域不得重画、滤镜化或替换内容
- 抽象面板优先保留关系、方向、节奏和负空间，而不是轮廓
- 面板保持 65%–80% 留白
- 标题仅出现一次，并作为构图标记参与画面
- 禁止纸纹、噪点、阴影、样机、Logo 和额外说明文字

完整规范见 [SKILL.md](./SKILL.md) 与 [references](./references)。

## 目录结构

```text
poetic-line-zine-poster/
├── SKILL.md
├── agents/
├── assets/
│   ├── style-references/
│   └── typography-references/
└── references/
```

## 素材说明

`assets/` 中的图片仅作为笔触和排版行为参考，不应复制其中的主体、文字、日期、颜色或整体版式。将仓库公开或用于商业项目之前，请自行确认所有参考素材的授权范围。
