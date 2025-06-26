def callback(commit):
    if b"Alice" in commit.author_name:
        commit.author_name = b"JunhoThemaster"
        commit.author_email = b"seojunho22@gmail.com"
    if b"Alice" in commit.committer_name:
        commit.committer_name = b"JunhoThemaster"
        commit.committer_email = b"seojunho22@gmail.com"
