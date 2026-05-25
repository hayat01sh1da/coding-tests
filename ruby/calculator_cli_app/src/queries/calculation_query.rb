# frozen_string_literal: true
# rbs_inline: enabled

require 'net/http'
require 'json'

module Queries
  class CalculationQuery
    # @rbs seed: String
    # @rbs return: void
    def initialize(seed)
      @seed = seed
    end

    # @rbs n: Integer
    # @rbs return: Integer
    def f(n)
      if n.zero?
        1
      elsif n == 2
        2
      elsif n.even?
        f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
      else
        ask_server(n)
      end
    end

    private

    attr_reader :seed

    # @rbs return: URI::Generic
    def uri
      @uri ||= URI.parse(ENV.fetch('CALCULATION_API'))
    end

    # @rbs n: Integer
    # @rbs return: Integer
    def ask_server(n)
      params    = { seed:, n: }
      uri.query = URI.encode_www_form(params)
      req       = Net::HTTP::Get.new(uri)
      res       = Net::HTTP.start(uri.host.to_s, uri.port) { |http| http.request(req) }
      JSON.parse(res.body)['result']
    end
  end
end
