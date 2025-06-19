document.addEventListener('DOMContentLoaded', () => {
  const profileDiv = document.getElementById('profile');
  const likeBtn = document.getElementById('like');
  const skipBtn = document.getElementById('skip');
  let currentProfile = null;

  async function loadProfile() {
    const userId = Telegram.WebApp.initDataUnsafe?.user?.id;
    const response = await fetch(`/profiles/random?user_id=${userId}`);
    if (response.ok) {
      currentProfile = await response.json();
      profileDiv.innerText = `${currentProfile.name} - ${currentProfile.city || ''}`;
    } else {
      profileDiv.innerText = 'No profiles';
    }
  }

  async function swipe(isLike) {
    if (!currentProfile) return;
    const userId = Telegram.WebApp.initDataUnsafe?.user?.id;
    await fetch(`/swipe?user_id=${userId}`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({to_user_id: currentProfile.id, is_like: isLike})
    });
    loadProfile();
  }

  likeBtn.addEventListener('click', () => swipe(true));
  skipBtn.addEventListener('click', () => swipe(false));

  loadProfile();
});
