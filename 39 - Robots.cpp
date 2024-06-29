#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
vector<vector<vector<int>>> mtrx;
vector<vector<int>> graph;

void bfs(int vert) {
  mtrx[vert][vert][0] = 0;
  deque<pair<int, int>> que;
  que.push_back({vert, 0});
  while (!que.empty()) {
    int ver = que.front().first;
    int step = que.front().second;
    que.pop_front();
    for (int j : graph[ver]) {
      if (step % 2 == 1) {
        if (mtrx[vert][j][0] > (step + 1)) {
          mtrx[vert][j][0] = step + 1;
          que.push_back({j, step + 1});
        }
      } else {
        if (mtrx[vert][j][1] > (step + 1)) {
          mtrx[vert][j][1] = step + 1;
          que.push_back({j, step + 1});
        }
      }
    }
  }
}

int main() {
  int n, k;
  cin >> n >> k;

  graph.resize(n);
  for (int i = 0; i < k; i++) {
    int a, b;
    cin >> a >> b;
    graph[a - 1].push_back(b - 1);
    graph[b - 1].push_back(a - 1);
  }

  int m;
  cin >> m;
  vector<int> robots(m);
  for (int i = 0; i < m; i++) {
    cin >> robots[i];
    robots[i]--;
  }

  mtrx.resize(n, vector<vector<int>>(n, vector<int>(2, INF)));
  for (int i : robots) {
    bfs(i);
  }

  priority_queue<float, vector<float>, greater<float>> minn;
  for (int j = 0; j < n; j++) {
    set<float> max_ch, max_nch;
    for (int i : robots) {
      max_ch.insert(mtrx[i][j][1]);
      max_nch.insert(mtrx[i][j][0]);
    }
    minn.push(min(*max_ch.rbegin(), *max_nch.rbegin()));
  }
  for (int i = 0; i < n; i++) {
    for (int j : graph[i]) {
      set<float> max_ch;
      for (int k : robots) {
        max_ch.insert((min(min(mtrx[k][i][0], mtrx[k][i][1]),
                           min(mtrx[k][j][0], mtrx[k][j][1])) +
                       0.5));
      }

      minn.push(*max_ch.rbegin());
    }
  }
  float otv = minn.top();
  if (otv == INF) {
    cout << -1 << endl;
  } else {
    cout << otv << endl;
  }
  return 0;
}