ready = input("""
      Welcome to your social media challenge. 
      In this challenge you will have a conversation with the machine.
      Let us test your ability to detect scammers online.

      Are you ready? (y or n): 
      """)

if ready == 'y':
    msg1 = input("""
    Hey friend, I have a problem that I need your help with. Can you help? (y or n):
    """)
    if msg1 == 'y':
        msg2 = input("""
        Great thank you! I have locked myself out of my GriffithPod account by mistake.
        I need your help resetting my password. Can you do that for me? (y or n): 
        """)

