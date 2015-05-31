# If the list grows large, it might be worth using a dictionary
isps = ('gmail.', 'yahoo.', 'earthlink.', 'comcast.', 'att.', 'movistar.', 'hotmail.', 'mail.', 'googlemail.',
        'msn.', 'bellsouth.', 'telus.', 'optusnet.', 'qq.', 'sky.', 'icloud.', 'mac.', 'sympatico.',
        'xtra.', 'web.', 'cox.', 'ymail.', 'aim.', 'rogers.', 'verizon.', 'rocketmail.', 'google.', 'optonline.',
        'sbcglobal.', 'aol.', 'me.', 'btinternet.', 'charter.', 'shaw.')

def is_isp_domain(domain):
  'Return True if the domain is a known ISP; False otherwise.'
  for isp in isps:
    if domain.startswith(isp):
      return True
  return False

def is_isp_email(email):
  'Return True if the domain for this email is a known ISP; False otherwise.'
  domain = email.split('@')[1]
  return is_isp_domain(domain)

