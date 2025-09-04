import random

topics = {
    "surname": {
        "liberal": [
            ("{{agent1}}", "夫婦別姓が認められないのは正直不便ですよね。名前を変えるたびに手続きも大変ですし…"),
            ("{{agent2}}", "そうなんです。結婚しても自分の名字を残したい方は多いので、社会に合わせて柔軟にした方が良いと思います"),
            ("{{agent3}}", "確かに、海外では当たり前で、日本でも制度を整えるべきかもしれませんね。{{user_name}}さんはどう思われますか。")
        ],
        "conservative": [
            ("{{agent1}}", "私は同じ姓を名乗るからこそ家族の一体感が保たれると思うんですよね。"),
            ("{{agent2}}", "そうですね。多少の不便はあっても、伝統や家族のつながりを守る方が大事かもしれません。"),
            ("{{agent3}}", "制度を大きく変えるよりも、現行制度の工夫で対応できる部分もありそうですし… {{user_name}}さんはいかがですか。")
        ]
    },
    "tourism": {
        "liberal": [
            ("{{agent1}}", "観光客をもっと受け入れた方が地域経済にプラスになりますよね。地方も潤いますし"),
            ("{{agent2}}", "本当ですね。インバウンドのおかげで小さなお店も助かっているところがあると思います。"),
            ("{{agent3}}", "文化交流にもつながりますし、国際的な印象も良くなるはずです。{{user_name}}さんはどう感じられますか。")
        ],
        "conservative": [
            ("{{agent1}}", "ただ、観光客が増えすぎると生活環境や治安への影響も心配になりますね。"),
            ("{{agent2}}", "確かに。地域のキャパシティを超えると住民に負担がかかりますし…"),
            ("{{agent3}}", "経済効果と環境負担のバランスをどう取るか、難しいところですよね。{{user_name}}さんはどう思われますか。")
        ]
    },
    "employment": {
        "liberal": [
            ("{{agent1}}", "終身雇用にこだわりすぎると、企業の柔軟性が失われてしまう気がします。"),
            ("{{agent2}}", "そう思います。個人にとっても転職の自由が広がった方がいいですよね。"),
            ("{{agent3}}", "世界的に見ても珍しい制度ですから、日本も変化を受け入れる時期かもしれませんね。{{user_name}}さんはいかがですか。")
        ],
        "conservative": [
            ("{{agent1}}", "やはり終身雇用があるからこそ安心して働けるという面は大きいですよね"),
            ("{{agent2}}", "うん、安定感があるからこそ、従業員も長期的に貢献につながっている気がします。"),
            ("{{agent3}}", "全面的な廃止ではなく、必要な部分だけを柔軟に変えるのが現実的かもしれませんね。{{user_name}}さんはどう思われますか。")
        ]
    },
    "medical": {
        "liberal": [
            ("{{agent1}}", "高齢者の医療費負担を少し見直さないと、現役世代との公平性が保てないですよね。"),
            ("{{agent2}}", "そうなんです。制度の持続性を考えると、ある程度の負担は避けられない気がします。"),
            ("{{agent3}}", "世代間のバランスをとる改革が必要かもしれませんね。{{user_name}}さんはどう思われますか。")
        ],
        "conservative": [
            ("{{agent1}}", "高齢者の方々は長年社会に貢献されてきたので、医療費の負担を増やすのは酷な気がします。"),
            ("{{agent2}}", "そうですね。安心して医療を受けられることが優先すべきだと思います"),
            ("{{agent3}}", "費用の問題は理解しますが、支え合いの精神を大事にしたいですよね。{{user_name}}さんはどう考えられますか。")
        ]
    },
    "nuclear": {
        "liberal": [
            ("{{agent1}}", "原発はリスクが大きすぎますし、再生可能エネルギーに移行すべきですよね。"),
            ("{{agent2}}", "そう思います。廃止には時間がかかっても、方向性をはっきり示すことが大切だと思います"),
            ("{{agent3}}", "環境面でも安全面でも、原発依存から脱却するのが望ましいですね。{{user_name}}さんはどうお考えですか。")
        ],
        "conservative": [
            ("{{agent1}}", "原発は安定した電力供給に欠かせないので、完全廃止は現実的ではないと思います。"),
            ("{{agent2}}", "再生可能エネルギーはまだ不安定ですし、当面は原発も必要ですよね.."),
            ("{{agent3}}", "安全対策を徹底しながら併用するのが妥当ではないでしょうか。{{user_name}}さんはどう思われますか。")
        ]
    }
}

def get_random_topic_and_messages(ideology, user_name, agent_names, topic=None):
    if topic is not None:
        topic_key = topic
    else:
        topic_key = random.choice(list(topics.keys()))

    messages = topics[topic_key][ideology]

    replacements = dict(zip(["{{agent1}}", "{{agent2}}", "{{agent3}}"], agent_names))

    formatted_messages = []
    for i, (speaker, line) in enumerate(messages):
        speaker_name = agent_names[i % 3]
        line = line.replace("{{user_name}}", user_name)
        for placeholder, real_name in replacements.items():
            line = line.replace(placeholder, real_name)
        formatted_messages.append((speaker_name, line))

    return topic_key, formatted_messages

