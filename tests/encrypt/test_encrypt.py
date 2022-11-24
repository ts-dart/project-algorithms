import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('message', 10) == 'egassem'
    assert encrypt_message('message', 5) == 'assem_eg'
    assert encrypt_message('message', 4) == 'ega_ssem'

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(message='message', key='key erro')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(message=00000, key=1)
